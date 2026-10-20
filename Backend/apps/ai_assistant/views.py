import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import MedicineAssistantQuerySerializer
from .services.gemini_service import GeminiMedicineAssistantService

logger = logging.getLogger(__name__)


class MedicineAssistantView(APIView):
    """
    POST /api/v1/ai-assistant/medicine/
    POST /api/ai-assistant/medicine/

    Accepts patient question, medicine context, target language, and conversation history.
    Returns AI-generated structured explanation using Google Gemini backend service.
    """
    permission_classes = [permissions.AllowAny]  # Allow all patient/guest users to access

    def post(self, request, *args, **kwargs):
        serializer = MedicineAssistantQuerySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "error": "Invalid request payload.",
                    "details": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        validated_data = serializer.validated_data
        question = validated_data.get("question")
        medicine_data = validated_data.get("medicine") or {}
        language = validated_data.get("language") or "English"
        conversation_history = validated_data.get("conversation_history") or []

        try:
            result = GeminiMedicineAssistantService.generate_medicine_explanation(
                question=question,
                medicine_data=medicine_data,
                language=language,
                conversation_history=conversation_history
            )

            return Response(
                {
                    "success": result.get("success", True),
                    "answer": result.get("answer", ""),
                    "medicine": result.get("medicine", ""),
                    "language": result.get("language", language),
                    "is_fallback": result.get("is_fallback", False)
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Error processing medicine assistant query: {str(e)}", exc_info=True)
            return Response(
                {
                    "success": False,
                    "error": "I'm unable to connect to the AI assistant right now. Please try again.",
                    "answer": "I'm unable to connect to the AI assistant right now. Please try again later or consult your doctor/pharmacist.",
                    "medicine": medicine_data.get("name") or medicine_data.get("medicine_name") or "",
                    "language": language
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AgenticAssistantView(APIView):
    """
    POST /api/v1/ai-assistant/agent/
    POST /api/ai-assistant/agent/

    Autonomous Healthcare Agent Endpoint (Meta Llama 3.3 ReAct Loop).
    Handles proactive voice check-ins, tool-calling (confirm_dose, trigger_sos),
    and Indic vernacular audio guidance.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        from .services.agentic_service import SwasthyaAgenticService

        message = request.data.get("message", "").strip()
        language = request.data.get("language", "hi")
        is_proactive = bool(request.data.get("is_proactive", False))
        patient_id = request.data.get("patient_id")

        patient = None
        if request.user and request.user.is_authenticated:
            try:
                patient = getattr(request.user, "patient_profile", None) or getattr(request.user, "patient", None)
            except Exception:
                pass

        if not patient and patient_id:
            try:
                from patients.models import Patient
                patient = Patient.objects.filter(id=patient_id).first()
            except Exception:
                pass

        try:
            result = SwasthyaAgenticService.run_agent(
                patient=patient,
                message=message,
                language=language,
                is_proactive=is_proactive,
                context=request.data.get("context")
            )
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in AgenticAssistantView: {e}", exc_info=True)
            return Response(
                {
                    "success": False,
                    "reply": "नमस्ते! आपका संदेश मिल गया है। कृपया थोड़ी देर बाद पुनः प्रयास करें।",
                    "audio_script": "नमस्ते! कृपया थोड़ी देर बाद पुनः प्रयास करें।",
                    "error": str(e)
                },
                status=status.HTTP_200_OK
            )
