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
      title: "Scan Doctor's Prescription",
      desc: 'Capture paper prescription slip via smartphone camera or ASHA worker tablet with instant edge-detection.',
      icon: DocumentIcon,
      color: 'from-teal-500 to-emerald-500',
      badge: '01 INTAKE',
    },
    {
      id: 2,
      num: '2',
      title: 'Clinical Vision OCR',
      desc: 'Neural optical model decodes complex doctor handwriting, medicine dosages (1-0-1, PC, TDS) & durations.',
      icon: BrainIcon,
      color: 'from-emerald-500 to-teal-600',
      badge: '02 OCR',
    },
    {
      id: 3,
      num: '3',
      title: 'Clinical Simplification',
      desc: 'Converts complex pharmaceutical jargon and Latin abbreviations into plain, clear mother-tongue terms.',
      icon: TranslateIcon,
      color: 'from-teal-600 to-cyan-600',
      badge: '03 TRANSLATE',
    },
    {
      id: 4,
      num: '4',
      title: '22+ Regional Voice Audio',
      desc: 'Natural synthesized voice playback in Hindi, Tamil, Telugu, Marathi & more for non-readers & elderly.',
      icon: SpeakerIcon,
      color: 'from-amber-500 to-orange-500',
      badge: '04 VOICE',
    },
    {
      id: 5,
      num: '5',
      title: 'Swasthya Mitr (AI Companion)',
      desc: 'Multilingual conversational AI answering food interactions, timing guidance, and medication precautions.',
      icon: SparklesIcon,
      color: 'from-amber-400 to-amber-600',
      badge: '05 CHAT',
    },
    {
      id: 6,
      num: '6',
      title: 'Smart Pillbox & Caregiver Sync',
      desc: 'Visual treatment schedules with SMS alerts, 2G IVR automated voice calls, and village ASHA registry.',
      icon: BellIcon,
      color: 'from-rose-500 to-teal-500',
      badge: '06 CARE',
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
      className="scroll-mt-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 font-sans relative py-12"
      onMouseEnter={() => setAutoPlay(false)}
      onMouseLeave={() => setAutoPlay(true)}
    >
      {/* SECTION HEADER */}
      <div className="text-center max-w-3xl mx-auto mb-12 space-y-2.5">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#0F766E]/10 dark:bg-teal-950/60 border border-[#0F766E]/30 text-[#0F766E] dark:text-teal-300 text-xs font-black tracking-widest uppercase shadow-2xs">
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

      {/* AMBIENT GLOW BACKDROP */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[550px] h-[550px] bg-gradient-to-tr from-teal-500/10 via-emerald-500/10 to-amber-500/5 blur-3xl rounded-full pointer-events-none -z-10" />

      {/* 3-COLUMN SHOWCASE: LEFT 3 CARDS | CENTER PHONE | RIGHT 3 CARDS */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        
        {/* LEFT FLANK: Steps 1, 2, 3 */}
        <div className="lg:col-span-4 space-y-4">
          {steps.slice(0, 3).map((s) => {
            const Icon = s.icon;
            const isActive = activeStep === s.id;
            return (
              <div
                key={s.id}
                onClick={() => setActiveStep(s.id)}
                className={`p-5 rounded-2xl border transition-all duration-300 cursor-pointer text-left relative overflow-hidden group ${
                  isActive
                    ? 'bg-white dark:bg-slate-900 border-[#0F766E] dark:border-teal-400 shadow-xl shadow-teal-500/10 scale-[1.02] ring-2 ring-[#0F766E]/20'
                    : 'bg-white/80 dark:bg-slate-900/70 border-slate-200/90 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 shadow-xs hover:shadow-md'
                }`}
              >
                {/* Active Indicator Bar */}
                {isActive && (
                  <div className="absolute top-0 left-0 bottom-0 w-1.5 bg-gradient-to-b from-[#0F766E] to-emerald-400" />
                )}

                <div className="flex items-center justify-between mb-2.5">
                  <div className="flex items-center gap-2.5">
                    <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-black text-xs transition-colors ${
                      isActive
                        ? 'bg-[#0F766E] text-white shadow-xs'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                    }`}>
                      {s.num}
                    </span>
                    <Icon size={18} className={isActive ? 'text-[#0F766E] dark:text-teal-400' : 'text-slate-500 dark:text-slate-400'} />
                  </div>
                  <span className="text-[10px] font-mono font-bold tracking-wider text-slate-400 dark:text-slate-500 uppercase">
                    {s.badge}
                  </span>
                </div>

                <h3 className={`text-base font-extrabold tracking-tight transition-colors ${
                  isActive ? 'text-[#0F766E] dark:text-teal-300' : 'text-slate-900 dark:text-white'
                }`}>
                  {s.title}
                </h3>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mt-1">
                  {s.desc}
                </p>
              </div>
            );
          })}
        </div>

        {/* CENTER: HYPER-REALISTIC SMARTPHONE MOCKUP */}
        <div className="lg:col-span-4 flex justify-center py-4">
          <div className="relative">
            {/* Luminous Phone Aura */}
            <div className="absolute inset-0 bg-teal-400/20 dark:bg-teal-500/15 blur-2xl rounded-[50px] transform scale-95 pointer-events-none" />

            {/* Phone Outer Chassis (Titanium Bezel) */}
            <div className="relative w-[300px] sm:w-[315px] rounded-[48px] p-3 bg-gradient-to-b from-slate-800 via-slate-900 to-slate-950 border-4 border-slate-700/80 shadow-[0_25px_60px_-15px_rgba(15,118,110,0.45)]">
              
              {/* Phone Inner Display Screen */}
              <div className="w-full h-[580px] rounded-[38px] bg-[#07131B] text-white flex flex-col overflow-hidden relative border border-slate-800 font-sans shadow-inner">
                
                {/* Dynamic Island Notch */}
                <div className="w-24 h-4 bg-black rounded-full mx-auto mt-2.5 mb-1.5 flex items-center justify-between px-2">
                  <span className="w-2 h-2 rounded-full bg-slate-900 border border-slate-700" />
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                </div>

                {/* Mockup Status Bar */}
                <div className="px-5 py-1 flex items-center justify-between text-[10px] font-mono text-slate-400">
                  <span className="font-bold text-white">9:41</span>
                  <div className="flex items-center gap-1.5">
                    <span>5G</span>
                    <span>100%</span>
                  </div>
                </div>

                {/* In-App App Bar */}
                <div className="px-4 py-2 border-b border-slate-800/80 flex items-center justify-between bg-slate-900/60 backdrop-blur-xs">
                  <div className="flex items-center gap-1.5">
                    <span className="w-6 h-6 rounded-lg bg-[#0F766E] flex items-center justify-center text-xs font-black">
                      🩺
                    </span>
                    <span className="text-xs font-black tracking-tight">Swasthya <span className="text-teal-400">AI</span></span>
                  </div>
                  <span className="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800/80 px-2 py-0.5 rounded-full font-bold">
                    Hindi (हिंदी)
                  </span>
                </div>

                {/* Interactive Flow Stepper at Top of Phone */}
                <div className="px-3 py-2 bg-slate-900/40 border-b border-slate-800/50 flex items-center justify-between">
                  {[1, 2, 3, 4, 5, 6].map((st) => (
                    <button
                      key={st}
                      onClick={() => setActiveStep(st)}
                      className={`w-6 h-6 rounded-full flex items-center justify-center text-[10px] font-black transition-all ${
                        activeStep === st
                          ? 'bg-gradient-to-r from-teal-400 to-emerald-400 text-slate-950 shadow-xs scale-110'
                          : activeStep > st
                          ? 'bg-teal-900/80 text-teal-300'
                          : 'bg-slate-800 text-slate-500'
                      }`}
                    >
                      {activeStep > st ? '✓' : st}
                    </button>
                  ))}
                </div>

                {/* Dynamic Screen Body based on activeStep */}
                <div className="flex-1 p-3.5 flex flex-col justify-between overflow-y-auto no-scrollbar">
                  
                  {/* STEP 1: SCAN DOCTOR'S SLIP */}
                  {activeStep === 1 && (
                    <div className="space-y-3 animate-fadeIn">
                      <div className="text-center pt-2">
                        <span className="text-[10px] bg-teal-950 text-teal-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                          Step 1 • Document Capture
                        </span>
                        <h4 className="text-sm font-black text-white mt-1">Optical Prescription Scanner</h4>
                      </div>

                      {/* Doctor Slip Frame with Scanning Laser */}
                      <div className="relative bg-white rounded-2xl p-3 text-slate-900 border-2 border-dashed border-teal-500/60 overflow-hidden shadow-lg">
                        <div className="flex items-center justify-between border-b border-slate-200 pb-1 mb-2">
                          <span className="text-xs font-serif font-black text-teal-800">℞ PHC Clinic</span>
                          <span className="text-[9px] font-mono text-slate-500">Dr. Sharma</span>
                        </div>
                        <div className="space-y-1 font-serif text-[11px] text-slate-700 italic">
                          <div>• Tab Paracetamol 650mg 1-0-1 PC (3d)</div>
                          <div>• Cap Amoxicillin 500mg 1-1-1 PC (5d)</div>
                          <div>• Tab Cetirizine 10mg 0-0-1 HS (3d)</div>
                        </div>
                        {/* Laser Scan Animation */}
                        <div className="absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-teal-500 to-transparent shadow-[0_0_12px_#14b8a6] animate-pulse top-1/2" />
                      </div>

                      <div className="bg-slate-900/90 p-2.5 rounded-xl border border-teal-500/30 text-center">
                        <span className="text-[11px] font-mono text-teal-300 font-bold flex items-center justify-center gap-1.5">
                          <span className="w-2 h-2 rounded-full bg-teal-400 animate-ping" />
                          <span>Auto-Detecting Prescription Edges...</span>
                        </span>
                      </div>
                    </div>
                  )}

                  {/* STEP 2: CLINICAL VISION OCR */}
                  {activeStep === 2 && (
                    <div className="space-y-3 animate-fadeIn">
                      <div className="text-center pt-2">
                        <span className="text-[10px] bg-emerald-950 text-emerald-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                          Step 2 • Vision OCR Parsing
                        </span>
                        <h4 className="text-sm font-black text-white mt-1">Handwriting Neural Extraction</h4>
                      </div>

                      <div className="space-y-2">
                        <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                          <div>
                            <div className="text-xs font-bold text-white">Paracetamol 650mg</div>
                            <div className="text-[10px] text-teal-400 font-mono">1-0-1 • Twice daily after meals</div>
                          </div>
                          <span className="text-[10px] bg-emerald-900/60 text-emerald-300 px-2 py-0.5 rounded font-mono font-bold">
                            99.4%
                          </span>
                        </div>

                        <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                          <div>
                            <div className="text-xs font-bold text-white">Amoxicillin 500mg</div>
                            <div className="text-[10px] text-teal-400 font-mono">1-1-1 • Thrice daily after food</div>
                          </div>
                          <span className="text-[10px] bg-emerald-900/60 text-emerald-300 px-2 py-0.5 rounded font-mono font-bold">
                            98.8%
                          </span>
                        </div>
                      </div>

                      <div className="text-center text-[10px] text-slate-400 font-mono">
                        ✓ Doctor signature and registration #84920 validated
                      </div>
                    </div>
                  )}

                  {/* STEP 3: VERNACULAR SIMPLIFICATION */}
                  {activeStep === 3 && (
                    <div className="space-y-3 animate-fadeIn">
                      <div className="text-center pt-2">
                        <span className="text-[10px] bg-cyan-950 text-cyan-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                          Step 3 • Clinical Simplification
                        </span>
                        <h4 className="text-sm font-black text-white mt-1">Plain Mother Tongue Guidance</h4>
                      </div>

                      <div className="bg-gradient-to-br from-teal-950/80 to-slate-900 p-3.5 rounded-2xl border border-teal-500/40 space-y-2">
                        <div className="text-[11px] font-mono text-teal-300 font-bold">
                          💊 खुराक की सरल जानकारी:
                        </div>
                        <div className="text-xs font-semibold text-slate-200 leading-relaxed">
                          सुबह नाश्ते के बाद और रात को खाने के बाद 1-1 गोली लें। बुखार उतरने पर बंद कर सकते हैं।
                        </div>
                      </div>

                      <div className="flex items-center justify-around text-center text-xs pt-1">
                        <div className="p-2 bg-slate-900 rounded-xl border border-slate-800 w-[48%]">
                          <div className="text-lg">☀️</div>
                          <div className="text-[10px] font-bold text-slate-300">सुबह 1 गोली</div>
                        </div>
                        <div className="p-2 bg-slate-900 rounded-xl border border-slate-800 w-[48%]">
                          <div className="text-lg">🌙</div>
                          <div className="text-[10px] font-bold text-slate-300">रात 1 गोली</div>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* STEP 4: 22+ REGIONAL AUDIO */}
                  {activeStep === 4 && (
                    <div className="space-y-3 animate-fadeIn text-center pt-2">
                      <span className="text-[10px] bg-amber-950 text-amber-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                        Step 4 • Voice Synthesis
                      </span>
                      <h4 className="text-sm font-black text-white">Audio in Your Mother Tongue</h4>

                      {/* Animated Soundwave Visualizer */}
                      <div className="p-4 bg-slate-900 rounded-2xl border border-amber-400/30 space-y-3">
                        <div className="flex items-center justify-center gap-1.5 h-12">
                          {[16, 32, 48, 28, 42, 50, 36, 20].map((h, i) => (
                            <div
                              key={i}
                              className="w-1.5 bg-gradient-to-t from-amber-500 to-amber-300 rounded-full animate-pulse"
                              style={{ height: `${h}px`, animationDelay: `${i * 0.1}s` }}
                            />
                          ))}
                        </div>
                        <div className="text-xs font-bold text-amber-300">
                          "नमस्ते, अपनी सुबह की दवा नाश्ते के बाद 1 गोली पानी से लें।"
                        </div>
                      </div>

                      <button
                        onClick={() => setIsPlayingAudio(!isPlayingAudio)}
                        className="w-full bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs py-2.5 rounded-xl shadow-md flex items-center justify-center gap-2"
                      >
                        <SpeakerIcon size={14} />
                        <span>{isPlayingAudio ? 'Pause Spoken Audio' : '🔊 Listen Voice Guidance'}</span>
                      </button>
                    </div>
                  )}

                  {/* STEP 5: SWASTHYA MITR (AI COMPANION) */}
                  {activeStep === 5 && (
                    <div className="space-y-3 animate-fadeIn">
                      <div className="text-center pt-2">
                        <span className="text-[10px] bg-amber-950 text-amber-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                          Step 5 • Conversational AI
                        </span>
                        <h4 className="text-sm font-black text-white mt-1">Swasthya Mitr Dialogue</h4>
                      </div>

                      {/* Chat Bubbles */}
                      <div className="space-y-2 text-xs">
                        <div className="bg-slate-800 p-2.5 rounded-2xl rounded-tl-xs max-w-[85%] text-slate-200">
                          क्या मैं यह दवा खाली पेट ले सकता हूँ?
                        </div>
                        <div className="bg-[#0F766E] p-2.5 rounded-2xl rounded-tr-xs max-w-[90%] ml-auto text-white leading-relaxed font-medium">
                          नहीं, डॉक्टर की सलाह के अनुसार यह दवा हमेशा भोजन या नाश्ते के बाद ही लेनी चाहिए ताकि पेट में जलन न हो।
                        </div>
                      </div>

                      {onOpenChat && (
                        <button
                          onClick={onOpenChat}
                          className="w-full bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs py-2 rounded-xl flex items-center justify-center gap-1.5 shadow-md"
                        >
                          <SparklesIcon size={14} />
                          <span>Open Live AI Health Assistant</span>
                        </button>
                      )}
                    </div>
                  )}

                  {/* STEP 6: SMART PILLBOX & ASHA SYNC */}
                  {activeStep === 6 && (
                    <div className="space-y-3 animate-fadeIn">
                      <div className="text-center pt-2">
                        <span className="text-[10px] bg-rose-950 text-rose-300 px-2.5 py-0.5 rounded-full font-mono uppercase font-bold">
                          Step 6 • Care Coordination
                        </span>
                        <h4 className="text-sm font-black text-white mt-1">Smart Pillbox & ASHA Sync</h4>
                      </div>

                      <div className="space-y-2 text-xs">
                        <div className="p-2 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                          <span className="text-slate-300">☀️ Morning Dose (8:30 AM)</span>
                          <span className="bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded font-bold">✓ Taken</span>
                        </div>
                        <div className="p-2 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                          <span className="text-slate-300">🌙 Night Dose (9:00 PM)</span>
                          <span className="bg-amber-950 text-amber-300 px-2 py-0.5 rounded font-bold">⏰ Pending</span>
                        </div>
                        <div className="p-2.5 rounded-xl bg-rose-950/40 border border-rose-900/60 flex items-center justify-between">
                          <div className="text-[11px] text-rose-200">
                            <span className="font-bold">ASHA Worker:</span> Sunita Devi notified
                          </div>
                          <span className="text-xs">👩‍⚕️</span>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Mockup Interactive Footer Input */}
                  <div className="pt-2 border-t border-slate-800/60 mt-auto">
                    <div 
                      onClick={onOpenChat}
                      className="bg-slate-900 rounded-full px-3 py-2 border border-slate-700/80 flex items-center justify-between text-xs text-slate-400 cursor-pointer hover:border-amber-400/50 transition-colors"
                    >
                      <span className="truncate">Ask Swasthya Mitr...</span>
                      <div className="w-5 h-5 rounded-full bg-amber-400 text-slate-950 flex items-center justify-center font-bold text-[10px]">
                        🎙️
                      </div>
                    </div>
                  </div>

                </div>

                {/* Phone Bottom Home Bar */}
                <div className="w-24 h-1 bg-slate-600 rounded-full mx-auto my-1.5" />
              </div>
            </div>
          </div>
        </div>

        {/* RIGHT FLANK: Steps 4, 5, 6 */}
        <div className="lg:col-span-4 space-y-4">
          {steps.slice(3, 6).map((s) => {
            const Icon = s.icon;
            const isActive = activeStep === s.id;
            return (
              <div
                key={s.id}
                onClick={() => setActiveStep(s.id)}
                className={`p-5 rounded-2xl border transition-all duration-300 cursor-pointer text-left relative overflow-hidden group ${
                  isActive
                    ? 'bg-white dark:bg-slate-900 border-[#0F766E] dark:border-teal-400 shadow-xl shadow-teal-500/10 scale-[1.02] ring-2 ring-[#0F766E]/20'
                    : 'bg-white/80 dark:bg-slate-900/70 border-slate-200/90 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 shadow-xs hover:shadow-md'
                }`}
              >
                {/* Active Indicator Bar */}
                {isActive && (
                  <div className="absolute top-0 left-0 bottom-0 w-1.5 bg-gradient-to-b from-[#0F766E] to-emerald-400" />
                )}

                <div className="flex items-center justify-between mb-2.5">
                  <div className="flex items-center gap-2.5">
                    <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-black text-xs transition-colors ${
                      isActive
                        ? 'bg-[#0F766E] text-white shadow-xs'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                    }`}>
                      {s.num}
                    </span>
                    <Icon size={18} className={isActive ? 'text-[#0F766E] dark:text-teal-400' : 'text-slate-500 dark:text-slate-400'} />
                  </div>
                  <span className="text-[10px] font-mono font-bold tracking-wider text-slate-400 dark:text-slate-500 uppercase">
                    {s.badge}
                  </span>
                </div>

                <h3 className={`text-base font-extrabold tracking-tight transition-colors ${
                  isActive ? 'text-[#0F766E] dark:text-teal-300' : 'text-slate-900 dark:text-white'
                }`}>
                  {s.title}
                </h3>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mt-1">
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
