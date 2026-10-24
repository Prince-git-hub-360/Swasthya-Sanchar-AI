import React, { useState, useEffect } from 'react';

/**
 * 🌟 CinematicIntroSplash
 * A high-impact opening experience for the Unleash LLM hackathon:
 * 1. Doctor Prescription Note (`Rx` handwriting)
 * 2. Luminous AI Laser Scanner sweeps down
 * 3. Handwriting dissolves into regional language scripts & audio waveforms
 * 4. The Official Swasthya Sanchar Logo emerges with an animated ECG heartbeat line!
 */
export const CinematicIntroSplash = ({ onFinish }) => {
  const [phase, setPhase] = useState('scan'); // 'scan' | 'transform' | 'logo' | 'exit'
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    // Stage 1 -> 2: Transform handwriting into regional letters & voice
    const timer1 = setTimeout(() => {
      setPhase('transform');
    }, 900);

    // Stage 2 -> 3: Reveal Swasthya Logo with ECG pulse
    const timer2 = setTimeout(() => {
      setPhase('logo');
    }, 1800);

    // Stage 3 -> Exit: Dissolve into app
    const timer3 = setTimeout(() => {
      setPhase('exit');
    }, 3100);

    // Complete & unmount
    const timer4 = setTimeout(() => {
      setVisible(false);
      if (onFinish) onFinish();
    }, 3500);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
      clearTimeout(timer3);
      clearTimeout(timer4);
    };
  }, [onFinish]);

  const handleSkip = () => {
    setPhase('exit');
    setTimeout(() => {
      setVisible(false);
      if (onFinish) onFinish();
    }, 250);
  };

  if (!visible) return null;

  return (
    <div
      onClick={handleSkip}
      className={`fixed inset-0 z-[9999] select-none flex flex-col items-center justify-center overflow-hidden transition-opacity duration-500 cursor-pointer ${
        phase === 'exit' ? 'opacity-0 pointer-events-none scale-105' : 'opacity-100'
      }`}
      style={{
        background: 'radial-gradient(ellipse at center, #062822 0%, #031411 70%, #010A08 100%)',
      }}
    >
      {/* Top Bar with Skip Hint & Hackathon Badge */}
      <div className="absolute top-4 left-0 right-0 px-5 flex items-center justify-between text-xs z-20 pointer-events-auto">
        <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-teal-950/60 border border-teal-500/30 text-teal-300 text-[10px] font-bold tracking-wider uppercase">
          <span className="w-1.5 h-1.5 rounded-full bg-teal-400 animate-pulse" />
          <span>Unleash LLM 2026</span>
        </div>

        <button
          type="button"
          onClick={handleSkip}
          className="text-slate-400 hover:text-white px-3 py-1 rounded-full bg-slate-900/60 border border-slate-700/60 text-[11px] font-semibold transition-colors"
        >
          Skip ➔
        </button>
      </div>

      {/* AMBIENT BACKGROUND GLOW */}
      <div className="absolute w-72 h-72 rounded-full bg-teal-500/10 blur-3xl pointer-events-none animate-pulse" />

      {/* ======================================================== */}
      {/* STAGE 1: DOCTOR PRESCRIPTION SCANNING (0.0s - 0.9s)      */}
      {/* ======================================================== */}
      {(phase === 'scan' || phase === 'transform') && (
        <div
          className={`relative w-72 sm:w-80 transition-all duration-700 transform flex flex-col items-center ${
            phase === 'transform' ? 'opacity-0 scale-90 translate-y-4 pointer-events-none' : 'opacity-100 scale-100'
          }`}
        >
          {/* Simulated Doctor Prescription Card */}
          <div className="w-full bg-white/95 rounded-2xl p-4 shadow-2xl border-2 border-teal-400/40 relative overflow-hidden text-slate-900 font-sans">
            {/* Header: Clinic Watermark */}
            <div className="flex items-center justify-between border-b border-slate-200 pb-2 mb-2">
              <div className="flex items-center gap-1.5">
                <span className="text-lg font-serif font-black text-teal-800">℞</span>
                <div>
                  <div className="text-[11px] font-bold text-slate-800 leading-tight">Rural PHC Clinic</div>
                  <div className="text-[9px] text-slate-500">Dr. Sharma, MBBS</div>
                </div>
              </div>
              <span className="text-[9px] font-mono bg-teal-50 text-teal-700 px-1.5 py-0.5 rounded border border-teal-200 font-bold">
                OPD #482
              </span>
            </div>

            {/* Handwritten Medical Notes (Doctor scribbles) */}
            <div className="space-y-1.5 my-2 font-serif italic text-slate-700 text-xs tracking-wide">
              <div className="flex items-center justify-between">
                <span>Tab Paracetamol 650mg</span>
                <span className="font-mono text-[10px] text-slate-500">1-0-1 (3d) PC</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Cap Amoxicillin 500mg</span>
                <span className="font-mono text-[10px] text-slate-500">1-1-1 (5d) PC</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Tab Cetirizine 10mg</span>
                <span className="font-mono text-[10px] text-slate-500">0-0-1 (3d) HS</span>
              </div>
            </div>

            {/* Doctor's Signature scribbles */}
            <div className="border-t border-slate-100 pt-1.5 flex justify-end">
              <span className="font-serif italic text-slate-400 text-[10px]">Signed: Dr. S.~~</span>
            </div>

            {/* Luminous Animated AI Laser Scanner Bar */}
            <div
              className="absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-teal-400 to-transparent shadow-[0_0_15px_#2dd4bf,0_0_30px_#14b8a6] pointer-events-none"
              style={{
                animation: 'aiLaserSweep 1.1s ease-in-out infinite alternate',
              }}
            />
          </div>

          {/* AI Scan Label below card */}
          <div className="mt-4 flex items-center gap-2 text-teal-300 text-xs font-mono font-bold tracking-wider">
            <span className="w-2 h-2 rounded-full bg-teal-400 animate-ping" />
            <span>AI SCANNING HANDWRITTEN PRESCRIPTION...</span>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* STAGE 2: FLOATING REGIONAL LETTERS & VOICE WAVES         */}
      {/* ======================================================== */}
      {phase === 'transform' && (
        <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none transition-all duration-500">
          {/* Floating Regional Indian Language Characters */}
          <div className="relative w-72 h-48 flex items-center justify-center">
            <span className="absolute text-2xl font-black text-teal-300 animate-bounce" style={{ top: '10%', left: '15%' }}>अ</span>
            <span className="absolute text-2xl font-black text-amber-300 animate-pulse" style={{ top: '15%', right: '20%' }}>க</span>
            <span className="absolute text-2xl font-black text-emerald-300 animate-ping" style={{ bottom: '25%', left: '20%' }}>త</span>
            <span className="absolute text-2xl font-black text-teal-200 animate-bounce" style={{ bottom: '15%', right: '25%' }}>क</span>
            <span className="absolute text-2xl font-black text-cyan-300 animate-pulse" style={{ top: '45%', left: '48%' }}>ব</span>

            {/* Animated Audio Equalizer Soundwave Bars */}
            <div className="flex items-center gap-1.5">
              {[18, 36, 52, 64, 48, 32, 58, 24].map((h, i) => (
                <div
                  key={i}
                  className="w-1.5 rounded-full bg-gradient-to-t from-teal-500 to-amber-300"
                  style={{
                    height: `${h}px`,
                    animation: `soundwavePulse 0.6s ease-in-out ${i * 0.08}s infinite alternate`,
                  }}
                />
              ))}
            </div>
          </div>

          <div className="mt-3 text-amber-300 font-mono text-xs font-bold tracking-wider flex items-center gap-1.5">
            <span>🎙️ CONVERTING TO 22+ NATIVE VOICE LANGUAGES...</span>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* STAGE 3: THE GRAND SWASTHYA SANCHAR LOGO REVEAL          */}
      {/* ======================================================== */}
      {(phase === 'logo' || phase === 'exit') && (
        <div
          className={`flex flex-col items-center text-center px-4 transition-all duration-700 transform ${
            phase === 'logo' ? 'opacity-100 scale-100 translate-y-0' : 'opacity-80 scale-105'
          }`}
        >
          {/* THE OFFICIAL LOGO EMBLEM with Golden Aura */}
          <div className="relative mb-4 group">
            {/* Glowing background ring */}
            <div className="absolute inset-0 rounded-3xl bg-teal-400/25 blur-xl animate-pulse" />

            <div className="relative w-24 h-24 sm:w-28 sm:h-28 rounded-3xl bg-gradient-to-br from-[#0B4F42] via-[#07382F] to-[#041F1A] border-2 border-teal-300/60 p-3.5 shadow-[0_0_35px_rgba(20,184,166,0.5)] flex items-center justify-center transform transition-transform duration-300">
              <img
                src="/assets/branding/swasthya-sanchar-mark-white.png"
                alt="Swasthya Sanchar Logo"
                className="w-full h-full object-contain filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.4)]"
                onError={(e) => {
                  // Graceful fallback to app icon if mark-white has issue
                  e.currentTarget.src = '/assets/branding/swasthya-sanchar-app-icon.png';
                }}
              />
            </div>
          </div>

          {/* BRAND TITLE LOCKUP */}
          <div className="flex items-center gap-2 mb-1">
            <span className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">Swasthya</span>
            <span className="text-2xl sm:text-3xl font-extrabold text-teal-400 tracking-tight">Sanchar</span>
            <span className="bg-teal-400/20 text-teal-300 border border-teal-300/40 text-[10px] font-black px-1.5 py-0.5 rounded-md uppercase tracking-wider">
              AI
            </span>
          </div>

          {/* TAGLINE */}
          <p className="text-xs sm:text-sm text-slate-300 font-medium tracking-wide max-w-xs mt-1">
            Healthcare that speaks your language
          </p>

          {/* DYNAMIC VITALITY ECG HEARTBEAT SVG */}
          <div className="w-56 h-8 my-2 flex items-center justify-center overflow-hidden">
            <svg viewBox="0 0 200 40" className="w-full h-full stroke-teal-400 fill-none stroke-[2.5]">
              <path
                d="M 0 20 L 60 20 L 70 8 L 80 32 L 90 4 L 100 36 L 110 20 L 200 20"
                style={{
                  strokeDasharray: '200',
                  strokeDashoffset: '200',
                  animation: 'ecgDraw 1.2s ease-out forwards',
                }}
              />
            </svg>
          </div>

          {/* STATUS PILL */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-900/40 border border-teal-500/30 text-teal-300 text-[11px] font-mono font-bold mt-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
            <span>AI Voice & Prescription Ready</span>
          </div>
        </div>
      )}

      {/* KEYFRAME ANIMATIONS STYLESHEET */}
      <style>{`
        @keyframes aiLaserSweep {
          0% { top: 0%; opacity: 0.9; }
          50% { opacity: 1; }
          100% { top: 96%; opacity: 0.9; }
        }
        @keyframes soundwavePulse {
          0% { transform: scaleY(0.4); opacity: 0.7; }
          100% { transform: scaleY(1.2); opacity: 1; }
        }
        @keyframes ecgDraw {
          to { stroke-dashoffset: 0; }
        }
      `}</style>
    </div>
  );
};

export default CinematicIntroSplash;
