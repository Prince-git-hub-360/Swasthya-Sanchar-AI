from django.urls import path
from .views import MedicineAssistantView, AgenticAssistantView

urlpatterns = [
    path('medicine/', MedicineAssistantView.as_view(), name='ai-medicine-assistant'),
    path('medicine', MedicineAssistantView.as_view(), name='ai-medicine-assistant-no-slash'),
    path('agent/', AgenticAssistantView.as_view(), name='ai-agentic-assistant'),
    path('agent', AgenticAssistantView.as_view(), name='ai-agentic-assistant-no-slash'),
]
