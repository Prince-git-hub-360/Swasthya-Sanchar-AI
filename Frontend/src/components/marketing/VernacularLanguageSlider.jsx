import React, { useState, useEffect } from 'react';

export const VernacularLanguageSlider = () => {
  const [logoRevealed, setLogoRevealed] = useState(false);

  useEffect(() => {
    // Trigger logo creation animation on mount / entry
    const timer = setTimeout(() => {
      setLogoRevealed(true);
    }, 400);
    return () => clearTimeout(timer);
  }, []);

  const languages = [
    { script: 'हिंदी', eng: 'Hindi', region: 'North & Central India', color: 'from-amber-500/10 to-orange-500/10 border-amber-200 dark:border-amber-900/60 text-amber-900 dark:text-amber-200' },
    { script: 'தமிழ்', eng: 'Tamil', region: 'Tamil Nadu', color: 'from-teal-500/10 to-emerald-500/10 border-teal-200 dark:border-teal-900/60 text-teal-900 dark:text-teal-200' },
    { script: 'తెలుగు', eng: 'Telugu', region: 'Andhra & Telangana', color: 'from-blue-500/10 to-cyan-500/10 border-blue-200 dark:border-blue-900/60 text-blue-900 dark:text-blue-200' },
    { script: 'বাংলা', eng: 'Bengali', region: 'West Bengal & Tripura', color: 'from-rose-500/10 to-pink-500/10 border-rose-200 dark:border-rose-900/60 text-rose-900 dark:text-rose-200' },
    { script: 'मराठी', eng: 'Marathi', region: 'Maharashtra', color: 'from-orange-500/10 to-amber-500/10 border-orange-200 dark:border-orange-900/60 text-orange-900 dark:text-orange-200' },
    { script: 'ಕನ್ನಡ', eng: 'Kannada', region: 'Karnataka', color: 'from-purple-500/10 to-violet-500/10 border-purple-200 dark:border-purple-900/60 text-purple-900 dark:text-purple-200' },
    { script: 'ગુજરાતી', eng: 'Gujarati', region: 'Gujarat', color: 'from-emerald-500/10 to-teal-500/10 border-emerald-200 dark:border-emerald-900/60 text-emerald-900 dark:text-emerald-200' },
    { script: 'മലയാളം', eng: 'Malayalam', region: 'Kerala', color: 'from-cyan-500/10 to-sky-500/10 border-cyan-200 dark:border-cyan-900/60 text-cyan-900 dark:text-cyan-200' },
    { script: 'ਪੰਜਾਬੀ', eng: 'Punjabi', region: 'Punjab', color: 'from-amber-500/10 to-yellow-500/10 border-amber-200 dark:border-amber-900/60 text-amber-900 dark:text-amber-200' },
    { script: 'ଓଡ଼ିଆ', eng: 'Odia', region: 'Odisha', color: 'from-teal-500/10 to-cyan-500/10 border-teal-200 dark:border-teal-900/60 text-teal-900 dark:text-teal-200' },
    { script: 'অসমীয়া', eng: 'Assamese', region: 'Assam', color: 'from-indigo-500/10 to-blue-500/10 border-indigo-200 dark:border-indigo-900/60 text-indigo-900 dark:text-indigo-200' },
    { script: 'اردو', eng: 'Urdu', region: 'Pan-India', color: 'from-emerald-500/10 to-green-500/10 border-emerald-200 dark:border-emerald-900/60 text-emerald-900 dark:text-emerald-200' },
    { script: 'भोजपुरी', eng: 'Bhojpuri', region: 'Bihar & UP', color: 'from-rose-500/10 to-red-500/10 border-rose-200 dark:border-rose-900/60 text-rose-900 dark:text-rose-200' },
    { script: 'मैथिली', eng: 'Maithili', region: 'Mithila & North Bihar', color: 'from-purple-500/10 to-pink-500/10 border-purple-200 dark:border-purple-900/60 text-purple-900 dark:text-purple-200' },
  ];

  const features = [
    { icon: '💊', hindi: 'खुराक निर्देश', eng: 'Vernacular Dosage Guide' },
    { icon: '🩺', hindi: 'डॉक्टर की पर्ची', eng: 'Doctor Slip Vision OCR' },
    { icon: '🔊', hindi: 'मातृभाषा ऑडियो', eng: 'Dialect Spoken Audio' },
    { icon: '🏥', hindi: 'जन औषधि बचत', eng: 'Jan Aushadhi 70%+ Savings' },
    { icon: '👩‍⚕️', hindi: 'आशा कार्यकर्ता सिंक', eng: 'ASHA Worker Portal' },
    { icon: '🚨', hindi: '108 आपातकालीन', eng: '2G Offline Emergency SOS' },
    { icon: '☀️', hindi: 'सुबह-रात रिमाइंडर', eng: 'Morning/Night Pillbox' },
    { icon: '📱', hindi: '2G ऑटोमेटेड कॉल', eng: 'IVR Voice Call Reminders' },
    { icon: '⚡', hindi: '100% बायो-इक्विवेलेंट', eng: 'ABDM Privacy Compliant' },
  ];

  // Duplicate arrays for seamless infinite looping
  const duplicatedLanguages = [...languages, ...languages];
  const duplicatedFeatures = [...features, ...features];

  return (
    <section className="relative py-14 overflow-hidden font-sans border-y border-slate-200/80 dark:border-slate-800/80 bg-gradient-to-b from-slate-50/50 via-white to-slate-50/50 dark:from-slate-950 dark:via-slate-900 dark:to-slate-950">
      
      {/* ======================================================== */}
      {/* 🌟 CINEMATIC BACKGROUND LOGO ASSEMBLY ANIMATION          */}
      {/* Logo sweeps from Right to Left into Center to Assemble   */}
      {/* ======================================================== */}
      <div className="absolute inset-0 flex items-center justify-center pointer-events-none overflow-hidden z-0">
        
        {/* Soft Radial Ambient Aura */}
        <div className="w-[500px] h-[500px] rounded-full bg-gradient-to-tr from-teal-400/15 via-emerald-300/15 to-amber-300/15 dark:from-teal-900/20 dark:via-emerald-950/20 dark:to-amber-950/10 blur-[90px]" />

        {/* The Animated Logo Emblem Converging from Right to Center */}
        <div className={`transition-all duration-1000 ease-out transform flex flex-col items-center justify-center ${
          logoRevealed 
            ? 'opacity-20 dark:opacity-25 translate-x-0 scale-100' 
            : 'opacity-0 translate-x-72 scale-75'
        }`}>
          {/* Animated Neon Stethoscope / Cross Watermark */}
          <div className="relative">
            <img 
              src="/assets/branding/swasthya-sanchar-mark.png" 
              alt="Swasthya Sanchar AI Emblem"
              className="w-48 sm:w-64 h-48 sm:h-64 object-contain filter drop-shadow-[0_0_40px_rgba(15,118,110,0.4)]"
              onError={(e) => {
                e.target.onerror = null;
                e.target.style.display = 'none';
              }}
            />
            {/* Glowing Heartbeat Pulse Trail */}
            <div className="absolute inset-0 flex items-center justify-center">
              <span className="w-56 h-56 rounded-full border border-teal-500/30 animate-ping opacity-30" />
            </div>
          </div>

          <div className="text-center mt-2">
            <span className="text-xs sm:text-sm font-black tracking-widest text-[#0F766E] uppercase font-mono">
              स्वास्थ्य संचार AI • SWASTHYA SANCHAR AI
            </span>
          </div>
        </div>
      </div>

      {/* SECTION HEADER */}
      <div className="relative z-10 text-center max-w-3xl mx-auto px-4 mb-8 space-y-2">
        <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-50 dark:bg-amber-950/70 border border-amber-300/80 dark:border-amber-700/60 text-amber-900 dark:text-amber-200 text-xs font-black tracking-widest uppercase shadow-2xs">
          <span>🇮🇳 MULTI-LINGUAL CLINICAL INTELLIGENCE</span>
        </div>
        <h3 className="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 dark:text-white tracking-tight">
          Bridging 22+ Indian Languages from Clinic to Village
        </h3>
        <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 max-w-xl mx-auto">
          Every prescription, medicine dosage, and precaution communicated clearly in the patient's mother tongue.
        </p>
      </div>

      {/* ======================================================== */}
      {/* ROW 1: SLIDING LEFT TO RIGHT (REGIONAL LANGUAGES)        */}
      {/* ======================================================== */}
      <div className="relative z-10 mb-4 overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_10%,black_90%,transparent)]">
        <div className="animate-marquee-left py-1 flex items-center gap-3 w-max">
          {duplicatedLanguages.map((lang, idx) => (
            <div
              key={`${lang.eng}-${idx}`}
              className={`shrink-0 flex items-center gap-2.5 px-4 py-2 rounded-2xl bg-white/90 dark:bg-slate-900/90 border shadow-xs hover:shadow-md hover:scale-105 transition-all duration-300 cursor-pointer backdrop-blur-md ${lang.color}`}
            >
              <span className="text-base font-black tracking-tight">{lang.script}</span>
              <span className="text-xs font-bold text-slate-700 dark:text-slate-300">• {lang.eng}</span>
              <span className="text-[10px] font-mono text-slate-400 dark:text-slate-500 hidden sm:inline">({lang.region})</span>
            </div>
          ))}
        </div>
      </div>

      {/* ======================================================== */}
      {/* ROW 2: SLIDING RIGHT TO LEFT (CLINICAL ACTIONS)          */}
      {/* ======================================================== */}
      <div className="relative z-10 overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_10%,black_90%,transparent)]">
        <div className="animate-marquee-right py-1 flex items-center gap-3 w-max">
          {duplicatedFeatures.map((feat, idx) => (
            <div
              key={`${feat.eng}-${idx}`}
              className="shrink-0 flex items-center gap-2.5 px-4 py-2 rounded-2xl bg-white/90 dark:bg-slate-900/90 border border-slate-200/90 dark:border-slate-800 shadow-xs hover:shadow-md hover:border-teal-400 hover:scale-105 transition-all duration-300 cursor-pointer backdrop-blur-md"
            >
              <span className="text-base">{feat.icon}</span>
              <span className="text-xs font-black text-slate-900 dark:text-white">{feat.hindi}</span>
              <span className="text-xs font-medium text-[#0F766E] dark:text-teal-300 font-mono">• {feat.eng}</span>
            </div>
          ))}
        </div>
      </div>

    </section>
  );
};

export default VernacularLanguageSlider;
