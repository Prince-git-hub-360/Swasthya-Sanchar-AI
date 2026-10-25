import React, { useState, useEffect } from 'react';
import { 
  DocumentIcon, BrainIcon, TranslateIcon, SpeakerIcon, 
  ClockIcon, BellIcon, SparklesIcon, CheckIcon, HeartIcon, ArrowRightIcon
} from '../../shared/icons/Icons';

export const InteractiveProductShowcase = ({ onOpenChat }) => {
  const [activeStep, setActiveStep] = useState(1);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);
  const [autoPlay, setAutoPlay] = useState(true);

  const steps = [
    {
      id: 1,
      num: '1',
      title: "Select a Prescription",
      desc: 'Digitally capture doctor slip via smartphone camera or ASHA worker tablet with instant edge-detection.',
      icon: DocumentIcon,
      badge: '01 INTAKE',
      glow: 'shadow-teal-500/15 border-teal-500/60',
      badgeBg: 'bg-teal-50 text-teal-800 border-teal-300 dark:bg-teal-950 dark:text-teal-200 dark:border-teal-700',
    },
    {
      id: 2,
      num: '2',
      title: 'Clinical Vision OCR',
      desc: 'Neural optical model decodes complex doctor handwriting, medicine dosages (1-0-1, PC, TDS) & durations.',
      icon: BrainIcon,
      badge: '02 VISION OCR',
      glow: 'shadow-emerald-500/15 border-emerald-500/60',
      badgeBg: 'bg-emerald-50 text-emerald-800 border-emerald-300 dark:bg-emerald-950 dark:text-emerald-200 dark:border-emerald-700',
    },
    {
      id: 3,
      num: '3',
      title: 'Medical Simplification',
      desc: 'Converts pharmaceutical jargon and Latin abbreviations into plain, clear mother-tongue instructions.',
      icon: TranslateIcon,
      badge: '03 SIMPLIFY',
      glow: 'shadow-cyan-500/15 border-cyan-500/60',
      badgeBg: 'bg-cyan-50 text-cyan-800 border-cyan-300 dark:bg-cyan-950 dark:text-cyan-200 dark:border-cyan-700',
    },
    {
      id: 4,
      num: '4',
      title: 'Transcribe to Native Audio',
      desc: 'Natural synthesized voice playback in Hindi, Tamil, Telugu, Marathi & more for non-readers & elderly.',
      icon: SpeakerIcon,
      badge: '04 VOICE',
      glow: 'shadow-amber-500/15 border-amber-500/60',
      badgeBg: 'bg-amber-50 text-amber-800 border-amber-300 dark:bg-amber-950 dark:text-amber-200 dark:border-amber-700',
    },
    {
      id: 5,
      num: '5',
      title: 'Talk to Prescription (AI)',
      desc: 'Engage in real-time multilingual dialogue answering food timing, interactions, and precautions.',
      icon: SparklesIcon,
      badge: '05 SWASTHYA MITR',
      glow: 'shadow-orange-500/15 border-orange-500/60',
      badgeBg: 'bg-orange-50 text-orange-800 border-orange-300 dark:bg-orange-950 dark:text-orange-200 dark:border-orange-700',
    },
    {
      id: 6,
      num: '6',
      title: 'Smart Pillbox & Caregiver',
      desc: 'Visual treatment schedules with SMS alerts, 2G IVR automated voice calls, and village ASHA sync.',
      icon: BellIcon,
      badge: '06 ADHERENCE',
      glow: 'shadow-rose-500/15 border-rose-500/60',
      badgeBg: 'bg-rose-50 text-rose-800 border-rose-300 dark:bg-rose-950 dark:text-rose-200 dark:border-rose-700',
    },
  ];

  // Auto-cycle through steps unless hovered
  useEffect(() => {
    if (!autoPlay) return;
    const interval = setInterval(() => {
      setActiveStep((prev) => (prev >= 6 ? 1 : prev + 1));
    }, 4500);
    return () => clearInterval(interval);
  }, [autoPlay]);

  return (
    <section 
      id="how-it-works" 
      className="scroll-mt-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 font-sans relative py-16"
      onMouseEnter={() => setAutoPlay(false)}
      onMouseLeave={() => setAutoPlay(true)}
    >
      {/* 🌟 WARM AMBIENT RADIANT BACKDROP GLOW (Just like the reference image) */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[750px] h-[650px] bg-gradient-to-tr from-amber-200/25 via-teal-200/25 to-emerald-100/30 dark:from-teal-950/20 dark:via-emerald-950/20 dark:to-amber-950/10 blur-[100px] rounded-full pointer-events-none -z-10" />

      {/* SECTION HEADER */}
      <div className="text-center max-w-3xl mx-auto mb-14 space-y-2.5">
        <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-teal-50 dark:bg-teal-950/60 border border-teal-200/80 dark:border-teal-700/60 text-[#0F766E] dark:text-teal-300 text-xs font-black tracking-widest uppercase shadow-xs">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          <span>CONNECTED HEALTHCARE PIPELINE</span>
        </div>
        <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 dark:text-white tracking-tight leading-tight">
          From Doctor’s Slip to Everyday Understanding
        </h2>
        <p className="text-sm sm:text-base text-slate-600 dark:text-slate-300 max-w-2xl mx-auto">
          A seamless 6-step communication journey engineered specifically for rural citizens, elderly patients, and ASHA health workers.
        </p>
      </div>

      {/* 3-COLUMN SHOWCASE: LEFT 3 CARDS | CENTER METALLIC PHONE | RIGHT 3 CARDS */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 items-center">
        
        {/* ======================================================== */}
        {/* LEFT FLANK: Steps 1, 2, 3                                */}
        {/* ======================================================== */}
        <div className="lg:col-span-4 space-y-5">
          {steps.slice(0, 3).map((s) => {
            const Icon = s.icon;
            const isActive = activeStep === s.id;
            return (
              <div
                key={s.id}
                onClick={() => setActiveStep(s.id)}
                className={`p-6 rounded-3xl border transition-all duration-300 cursor-pointer text-left relative overflow-hidden backdrop-blur-md ${
                  isActive
                    ? `bg-white dark:bg-slate-900 border-[#0F766E] dark:border-teal-400 shadow-[0_16px_40px_-8px_rgba(15,118,110,0.22),0_0_20px_rgba(20,184,166,0.18)] scale-[1.03] ring-2 ring-[#0F766E]/20`
                    : `bg-white/80 dark:bg-slate-900/70 border-slate-200/80 dark:border-slate-800 shadow-[0_8px_24px_-6px_rgba(0,0,0,0.04)] hover:shadow-[0_12px_32px_-6px_rgba(15,118,110,0.12)] hover:border-teal-300 dark:hover:border-slate-700 hover:scale-[1.01]`
                }`}
              >
                {/* Active Indicator Bar */}
                {isActive && (
                  <div className="absolute top-0 left-0 bottom-0 w-1.5 bg-gradient-to-b from-[#0F766E] to-emerald-400" />
                )}

                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <span className={`w-8 h-8 rounded-xl flex items-center justify-center font-black text-xs border transition-colors ${
                      isActive
                        ? 'bg-[#0F766E] text-white border-[#0F766E] shadow-sm'
                        : s.badgeBg
                    }`}>
                      {s.num}
                    </span>
                    <Icon size={20} className={isActive ? 'text-[#0F766E] dark:text-teal-400' : 'text-slate-500 dark:text-slate-400'} />
                  </div>
                  <span className="text-[10px] font-mono font-bold tracking-wider text-slate-400 dark:text-slate-500 uppercase">
                    {s.badge}
                  </span>
                </div>

                <h3 className={`text-base sm:text-lg font-black tracking-tight transition-colors ${
                  isActive ? 'text-[#0F766E] dark:text-teal-300' : 'text-slate-900 dark:text-white'
                }`}>
                  {s.title}
                </h3>
                <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed mt-1.5 font-normal">
                  {s.desc}
                </p>
              </div>
            );
          })}
        </div>

        {/* ======================================================== */}
        {/* CENTER: CHAMPAGNE-GOLD METALLIC PHONE + RADIANT SCREEN   */}
        {/* ======================================================== */}
        <div className="lg:col-span-4 flex justify-center py-4">
          <div className="relative">
            
            {/* Luminous Warm Diffuse Halo */}
            <div className="absolute inset-0 bg-gradient-to-b from-amber-300/30 via-teal-300/30 to-emerald-300/20 blur-3xl rounded-[60px] transform scale-95 pointer-events-none" />

            {/* Premium Metallic Titanium-Gold Chassis (Reflective Bezel) */}
            <div className="relative w-[305px] sm:w-[325px] rounded-[52px] p-2.5 bg-gradient-to-b from-[#E7CF9E] via-[#D8B46C] to-[#996C36] shadow-[0_25px_60px_-12px_rgba(180,130,50,0.35),0_15px_30px_-8px_rgba(15,118,110,0.25)] border-2 border-[#F7E7C4]">
              
              {/* Inner Metallic Bezel Ring */}
              <div className="rounded-[44px] p-1 bg-gradient-to-b from-slate-900 via-slate-950 to-black shadow-inner">
                
                {/* 🌟 BRIGHT, RADIANT LIGHT HEALTHCARE SCREEN (Warm & Friendly!) */}
                <div className="w-full h-[600px] rounded-[40px] bg-gradient-to-b from-[#FFFFFF] via-[#F8FAFC] to-[#F1F5F9] text-slate-900 flex flex-col overflow-hidden relative font-sans shadow-inner border border-slate-200/60">
                  
                  {/* Dynamic Island Notch */}
                  <div className="w-22 h-4 bg-black rounded-full mx-auto mt-2 mb-1 flex items-center justify-between px-2.5 shadow-xs">
                    <span className="w-2 h-2 rounded-full bg-slate-900 border border-slate-700" />
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                  </div>

                  {/* Status Bar */}
                  <div className="px-5 py-0.5 flex items-center justify-between text-[10px] font-mono text-slate-600 font-bold">
                    <span>9:41</span>
                    <div className="flex items-center gap-1.5">
                      <span>5G</span>
                      <span className="text-[11px]">🔋</span>
                    </div>
                  </div>

                  {/* Top Healthcare App Bar */}
                  <div className="px-4 py-2 border-b border-slate-200/80 flex items-center justify-between bg-white/90 backdrop-blur-md">
                    <div className="flex items-center gap-1.5">
                      <span className="w-6 h-6 rounded-lg bg-[#0F766E] flex items-center justify-center text-xs text-white font-black shadow-xs">
                        🩺
                      </span>
                      <span className="text-xs font-black tracking-tight text-slate-900">
                        Swasthya <span className="text-[#0F766E]">AI</span>
                      </span>
                    </div>
                    <span className="text-[9px] bg-teal-50 text-[#0F766E] border border-teal-200 px-2 py-0.5 rounded-full font-bold">
                      Hindi (हिंदी)
                    </span>
                  </div>

                  {/* 🌟 Stepper Track Matching Reference Image */}
                  <div className="px-3 py-2 bg-slate-100/70 border-b border-slate-200/60 flex items-center justify-between">
                    {[1, 2, 3, 4, 5, 6].map((st) => (
                      <button
                        key={st}
                        onClick={() => setActiveStep(st)}
                        className={`w-6 h-6 rounded-full flex items-center justify-center text-[10px] font-black transition-all ${
                          activeStep === st
                            ? 'bg-gradient-to-r from-[#0F766E] to-emerald-500 text-white shadow-md scale-110 ring-2 ring-teal-400/30'
                            : activeStep > st
                            ? 'bg-teal-100 text-teal-800'
                            : 'bg-white text-slate-400 border border-slate-200'
                        }`}
                      >
                        {activeStep > st ? '✓' : st}
                      </button>
                    ))}
                  </div>

                  {/* 🌟 Namaste Greeting Header (Like Reference Image) */}
                  <div className="pt-2 pb-1 text-center">
                    <span className="text-xl">🙏</span>
                    <h4 className="text-xs font-black text-slate-900 tracking-tight mt-0.5">
                      Namaste! What can Swasthya AI help with?
                    </h4>
                    <span className="inline-block mt-0.5 text-[9px] font-extrabold bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 px-2 py-0.5 rounded-full shadow-2xs">
                      ✦ Rural Healthcare AI Companion
                    </span>
                  </div>

                  {/* Screen Body Content Based on activeStep */}
                  <div className="flex-1 px-3.5 py-1.5 flex flex-col justify-between overflow-y-auto no-scrollbar">
                    
                    {/* STEP 1: SELECT A PRESCRIPTION */}
                    {activeStep === 1 && (
                      <div className="space-y-2.5 animate-fadeIn">
                        {/* Doctor Slip with Scanning Laser */}
                        <div className="relative bg-white rounded-2xl p-3 text-slate-900 border border-teal-200 shadow-md overflow-hidden">
                          <div className="flex items-center justify-between border-b border-slate-100 pb-1 mb-2">
                            <span className="text-xs font-serif font-black text-teal-900">℞ Primary Health Centre</span>
                            <span className="text-[9px] font-mono text-slate-500">Dr. Sharma, MBBS</span>
                          </div>
                          <div className="space-y-1 font-serif text-[11px] text-slate-700 italic">
                            <div>• Tab Paracetamol 650mg 1-0-1 PC (3d)</div>
                            <div>• Cap Amoxicillin 500mg 1-1-1 PC (5d)</div>
                            <div>• Tab Cetirizine 10mg 0-0-1 HS (3d)</div>
                          </div>
                          {/* Animated Luminous Laser Scan Bar */}
                          <div className="absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-[#0F766E] to-transparent shadow-[0_0_12px_#14b8a6] animate-pulse top-1/2" />
                        </div>

                        <div className="bg-teal-50/80 p-2.5 rounded-xl border border-teal-200 text-center">
                          <span className="text-[11px] font-mono text-[#0F766E] font-bold flex items-center justify-center gap-1.5">
                            <span className="w-2 h-2 rounded-full bg-[#0F766E] animate-ping" />
                            <span>Prescription Auto-Detection Active</span>
                          </span>
                        </div>
                      </div>
                    )}

                    {/* STEP 2: CLINICAL VISION OCR */}
                    {activeStep === 2 && (
                      <div className="space-y-2 animate-fadeIn">
                        <div className="space-y-1.5">
                          <div className="p-2.5 rounded-xl bg-white border border-slate-200 shadow-xs flex items-center justify-between">
                            <div>
                              <div className="text-xs font-extrabold text-slate-900">Paracetamol 650mg</div>
                              <div className="text-[10px] text-teal-700 font-bold">1-0-1 • Twice daily after meals</div>
                            </div>
                            <span className="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full font-mono font-bold">
                              99.4%
                            </span>
                          </div>

                          <div className="p-2.5 rounded-xl bg-white border border-slate-200 shadow-xs flex items-center justify-between">
                            <div>
                              <div className="text-xs font-extrabold text-slate-900">Amoxicillin 500mg</div>
                              <div className="text-[10px] text-teal-700 font-bold">1-1-1 • Thrice daily after food</div>
                            </div>
                            <span className="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full font-mono font-bold">
                              98.8%
                            </span>
                          </div>
                        </div>

                        <div className="text-center text-[10px] text-slate-500 font-medium">
                          ✓ Validated against National Formulary (Jan Aushadhi)
                        </div>
                      </div>
                    )}

                    {/* STEP 3: MEDICAL SIMPLIFICATION */}
                    {activeStep === 3 && (
                      <div className="space-y-2.5 animate-fadeIn">
                        <div className="bg-gradient-to-br from-teal-50 to-emerald-50 p-3 rounded-2xl border border-teal-200 space-y-1.5 shadow-xs">
                          <div className="text-[10px] font-mono text-[#0F766E] font-black uppercase tracking-wider">
                            💊 सरल खुराक निर्देश (Hindi):
                          </div>
                          <div className="text-xs font-bold text-slate-800 leading-relaxed">
                            सुबह नाश्ते के बाद और रात को खाने के बाद 1-1 गोली पानी से लें।
                          </div>
                        </div>

                        <div className="flex items-center justify-around text-center text-xs">
                          <div className="p-2 bg-white rounded-xl border border-slate-200 shadow-2xs w-[48%]">
                            <div className="text-lg">☀️</div>
                            <div className="text-[10px] font-bold text-slate-800">सुबह 1 गोली</div>
                            <div className="text-[9px] text-slate-500">नाश्ते के बाद</div>
                          </div>
                          <div className="p-2 bg-white rounded-xl border border-slate-200 shadow-2xs w-[48%]">
                            <div className="text-lg">🌙</div>
                            <div className="text-[10px] font-bold text-slate-800">रात 1 गोली</div>
                            <div className="text-[9px] text-slate-500">भोजन के बाद</div>
                          </div>
                        </div>
                      </div>
                    )}

                    {/* STEP 4: TRANSCRIBE TO NATIVE AUDIO */}
                    {activeStep === 4 && (
                      <div className="space-y-2.5 animate-fadeIn text-center">
                        {/* Audio Waveform Card */}
                        <div className="p-3 bg-amber-50/80 rounded-2xl border border-amber-200 space-y-2 shadow-xs">
                          <div className="flex items-center justify-center gap-1.5 h-10">
                            {[14, 28, 44, 24, 38, 46, 32, 18].map((h, i) => (
                              <div
                                key={i}
                                className="w-1.5 bg-gradient-to-t from-amber-500 to-amber-600 rounded-full animate-pulse"
                                style={{ height: `${h}px`, animationDelay: `${i * 0.1}s` }}
                              />
                            ))}
                          </div>
                          <div className="text-[11px] font-bold text-amber-900 leading-tight">
                            "नमस्ते, अपनी सुबह की दवा नाश्ते के बाद 1 गोली पानी से लें।"
                          </div>
                        </div>

                        <button
                          onClick={() => setIsPlayingAudio(!isPlayingAudio)}
                          className="w-full bg-[#0F766E] hover:bg-[#0A4D48] text-white font-black text-xs py-2 rounded-xl shadow-xs flex items-center justify-center gap-2"
                        >
                          <SpeakerIcon size={14} color="#fff" />
                          <span>{isPlayingAudio ? 'Playing Spoken Voice...' : '🔊 Listen Audio Guidance'}</span>
                        </button>
                      </div>
                    )}

                    {/* STEP 5: TALK TO PRESCRIPTION (AI COMPANION) */}
                    {activeStep === 5 && (
                      <div className="space-y-2 animate-fadeIn text-xs">
                        <div className="space-y-2">
                          <div className="bg-slate-100 p-2.5 rounded-2xl rounded-tl-xs max-w-[85%] text-slate-800 font-medium">
                            क्या मैं यह दवा खाली पेट ले सकता हूँ?
                          </div>
                          <div className="bg-[#0F766E] p-2.5 rounded-2xl rounded-tr-xs max-w-[90%] ml-auto text-white leading-relaxed font-semibold shadow-xs">
                            नहीं, डॉक्टर की सलाह के अनुसार यह दवा हमेशा भोजन के बाद ही लें ताकि पेट में जलन न हो।
                          </div>
                        </div>

                        {onOpenChat && (
                          <button
                            onClick={onOpenChat}
                            className="w-full bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs py-2 rounded-xl shadow-xs flex items-center justify-center gap-1.5"
                          >
                            <SparklesIcon size={14} />
                            <span>Ask Live AI Medical Assistant</span>
                          </button>
                        )}
                      </div>
                    )}

                    {/* STEP 6: SMART PILLBOX & CAREGIVER */}
                    {activeStep === 6 && (
                      <div className="space-y-2 animate-fadeIn text-xs">
                        <div className="space-y-1.5">
                          <div className="p-2 rounded-xl bg-white border border-slate-200 shadow-2xs flex items-center justify-between">
                            <span className="font-semibold text-slate-800">☀️ Morning Dose (8:30 AM)</span>
                            <span className="bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full font-bold text-[10px]">✓ Taken</span>
                          </div>
                          <div className="p-2 rounded-xl bg-white border border-slate-200 shadow-2xs flex items-center justify-between">
                            <span className="font-semibold text-slate-800">🌙 Night Dose (9:00 PM)</span>
                            <span className="bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full font-bold text-[10px]">⏰ Pending</span>
                          </div>
                          <div className="p-2 rounded-xl bg-rose-50 border border-rose-200 flex items-center justify-between">
                            <span className="text-[11px] font-bold text-rose-900">ASHA Worker: Sunita Devi Notified</span>
                            <span className="text-xs">👩‍⚕️</span>
                          </div>
                        </div>
                      </div>
                    )}

                    {/* 🌟 Bottom Conversational Bar (Exact Layout from Reference Image!) */}
                    <div className="pt-2 border-t border-slate-200/80 mt-auto">
                      <div 
                        onClick={onOpenChat}
                        className="bg-white rounded-full px-3 py-1.5 border border-slate-300 shadow-sm flex items-center justify-between text-xs text-slate-500 cursor-pointer hover:border-[#0F766E] transition-colors"
                      >
                        <span className="truncate text-[11px] font-medium">Ask Swasthya Mitr...</span>
                        
                        <div className="flex items-center gap-1.5 shrink-0">
                          <span className="text-[10px] font-bold bg-slate-100 px-1.5 py-0.5 rounded text-slate-600">
                            हि ▾
                          </span>
                          <div className="w-5 h-5 rounded-full bg-gradient-to-r from-amber-400 to-amber-500 text-slate-950 flex items-center justify-center font-bold text-[10px] shadow-2xs">
                            🎙️
                          </div>
                          <div className="w-5 h-5 rounded-full bg-[#0F766E] text-white flex items-center justify-center font-bold text-[10px] shadow-2xs">
                            ➔
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>

                  {/* Phone Bottom Home Bar Indicator */}
                  <div className="w-24 h-1 bg-slate-400 rounded-full mx-auto my-1.5" />
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* ======================================================== */}
        {/* RIGHT FLANK: Steps 4, 5, 6                               */}
        {/* ======================================================== */}
        <div className="lg:col-span-4 space-y-5">
          {steps.slice(3, 6).map((s) => {
            const Icon = s.icon;
            const isActive = activeStep === s.id;
            return (
              <div
                key={s.id}
                onClick={() => setActiveStep(s.id)}
                className={`p-6 rounded-3xl border transition-all duration-300 cursor-pointer text-left relative overflow-hidden backdrop-blur-md ${
                  isActive
                    ? `bg-white dark:bg-slate-900 border-[#0F766E] dark:border-teal-400 shadow-[0_16px_40px_-8px_rgba(15,118,110,0.22),0_0_20px_rgba(20,184,166,0.18)] scale-[1.03] ring-2 ring-[#0F766E]/20`
                    : `bg-white/80 dark:bg-slate-900/70 border-slate-200/80 dark:border-slate-800 shadow-[0_8px_24px_-6px_rgba(0,0,0,0.04)] hover:shadow-[0_12px_32px_-6px_rgba(15,118,110,0.12)] hover:border-teal-300 dark:hover:border-slate-700 hover:scale-[1.01]`
                }`}
              >
                {/* Active Indicator Bar */}
                {isActive && (
                  <div className="absolute top-0 left-0 bottom-0 w-1.5 bg-gradient-to-b from-[#0F766E] to-emerald-400" />
                )}

                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <span className={`w-8 h-8 rounded-xl flex items-center justify-center font-black text-xs border transition-colors ${
                      isActive
                        ? 'bg-[#0F766E] text-white border-[#0F766E] shadow-sm'
                        : s.badgeBg
                    }`}>
                      {s.num}
                    </span>
                    <Icon size={20} className={isActive ? 'text-[#0F766E] dark:text-teal-400' : 'text-slate-500 dark:text-slate-400'} />
                  </div>
                  <span className="text-[10px] font-mono font-bold tracking-wider text-slate-400 dark:text-slate-500 uppercase">
                    {s.badge}
                  </span>
                </div>

                <h3 className={`text-base sm:text-lg font-black tracking-tight transition-colors ${
                  isActive ? 'text-[#0F766E] dark:text-teal-300' : 'text-slate-900 dark:text-white'
                }`}>
                  {s.title}
                </h3>
                <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed mt-1.5 font-normal">
                  {s.desc}
                </p>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
};

export default InteractiveProductShowcase;
