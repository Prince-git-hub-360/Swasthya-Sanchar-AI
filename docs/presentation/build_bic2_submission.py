import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_THEME_COLOR

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ==============================================================================
# UNIFIED LUXURY DARK TEAL & MEDICAL CYAN PALETTE (MATCHING SLIDES 1-3)
# ==============================================================================
C_BG_DARK     = RGBColor(8, 30, 36)        # #081E24 - Deep Medical Obsidian Teal (Deck BG)
C_CARD_DARK   = RGBColor(14, 48, 56)       # #0E3038 - Elevated Surface Dark Teal
C_CARD_DEEP   = RGBColor(10, 38, 45)       # #0A262D - Sub-panel Dark Teal
C_BORDER_TEAL = RGBColor(27, 94, 109)      # #1B5E6D - Subtle Glowing Teal Border
C_BORDER_CYAN = RGBColor(45, 212, 191)     # #2DD4BF - Accent Bright Cyan Border

C_CYAN_ACCENT = RGBColor(45, 212, 191)     # #2DD4BF - Primary Accent Cyan / Mint
C_SAFFRON     = RGBColor(245, 158, 11)     # #F59E0B - Warm Amber / Saffron Accent
C_WHITE       = RGBColor(255, 255, 255)    # #FFFFFF - Crisp Title White
C_ICE_TEXT    = RGBColor(226, 232, 240)    # #E2E8F0 - High Legibility Body Slate/White
C_MUTED_CYAN  = RGBColor(148, 187, 196)    # #94BBC4 - Metadata / Secondary Text
C_GREEN       = RGBColor(52, 211, 153)     # #34D399 - Success Emerald
C_RED         = RGBColor(248, 113, 113)    # #F87171 - Urgent Crimson

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "docs", "report_screenshots")

def build_perfect_presentation(pptx_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_dark_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_DARK
        bg.line.fill.background()
        return bg

    def add_dark_header(slide, slide_num, title, subtitle=None):
        set_slide_dark_background(slide)

        # Top subtle cyan-teal accent gradient line
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_CYAN_ACCENT
        top_bar.line.fill.background()

        # Top Left Category Badge
        cat_badge = slide.shapes.add_textbox(Inches(0.8), Inches(0.25), Inches(11.7), Inches(0.35))
        cbtf = cat_badge.text_frame
        cbtf.margin_left = cbtf.margin_top = cbtf.margin_right = cbtf.margin_bottom = 0
        cbp = cbtf.paragraphs[0]
        cbr = cbp.add_run()
        cbr.text = f"BHARAT INNOVATION CHALLENGE 2.0  •  {f'0{slide_num}' if slide_num < 10 else slide_num} {title.upper()}"
        cbr.font.name = "Segoe UI"
        cbr.font.size = Pt(9.5)
        cbr.font.bold = True
        cbr.font.color.rgb = C_CYAN_ACCENT

        # Header Title container
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.7), Inches(0.85))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        run_title = p.add_run()
        run_title.text = title
        run_title.font.name = "Segoe UI"
        run_title.font.size = Pt(22)
        run_title.font.bold = True
        run_title.font.color.rgb = C_WHITE

        if subtitle:
            p2 = tf.add_paragraph()
            p2.space_before = Pt(2)
            run_sub = p2.add_run()
            run_sub.text = subtitle
            run_sub.font.name = "Segoe UI"
            run_sub.font.size = Pt(11)
            run_sub.font.color.rgb = C_ICE_TEXT

        # Consistent Dark Footer
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.7), Inches(0.3))
        ftf = footer_box.text_frame
        ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
        fp = ftf.paragraphs[0]
        fr1 = fp.add_run()
        fr1.text = "SWASTHYA SANCHAR  •  Change_The_World"
        fr1.font.name = "Segoe UI"
        fr1.font.size = Pt(9)
        fr1.font.color.rgb = C_MUTED_CYAN

        fr_page = fp.add_run()
        fr_page.text = f"{' ' * 130}{slide_num} / 12"
        fr_page.font.name = "Segoe UI"
        fr_page.font.size = Pt(9)
        fr_page.font.bold = True
        fr_page.font.color.rgb = C_MUTED_CYAN

    def add_card(slide, left, top, width, height, bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(border_width)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: COVER SLIDE (STRICT COMPLIANCE - NO SCHOOL NAME)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_dark_background(slide1)

    # Top accent line
    top_bar1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
    top_bar1.fill.solid()
    top_bar1.fill.fore_color.rgb = C_CYAN_ACCENT
    top_bar1.line.fill.background()

    # Track badge
    badge1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(4.8), Inches(0.42))
    badge1.fill.solid()
    badge1.fill.fore_color.rgb = C_CARD_DARK
    badge1.line.color.rgb = C_BORDER_TEAL
    b1tf = badge1.text_frame
    b1tf.margin_left = Inches(0.15)
    b1tf.margin_top = Inches(0.08)
    bp1 = b1tf.paragraphs[0]
    br1 = bp1.add_run()
    br1.text = "BHARAT INNOVATION CHALLENGE 2.0  •  HEALTHTECH & AI"
    br1.font.name = "Segoe UI"
    br1.font.size = Pt(9.5)
    br1.font.bold = True
    br1.font.color.rgb = C_CYAN_ACCENT

    # Brand Title
    s1_title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(6.8), Inches(2.2))
    s1_ttf = s1_title_box.text_frame
    s1_ttf.word_wrap = True
    s1_ttf.margin_left = s1_ttf.margin_top = s1_ttf.margin_right = s1_ttf.margin_bottom = 0
    
    p1 = s1_ttf.paragraphs[0]
    r1 = p1.add_run()
    r1.text = "SWASTHYA SANCHAR\n"
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(32)
    r1.font.bold = True
    r1.font.color.rgb = C_WHITE

    p1_sub = s1_ttf.add_paragraph()
    p1_sub.space_before = Pt(4)
    r1_sub = p1_sub.add_run()
    r1_sub.text = "AI-Powered Healthcare Communication Assistant for Rural Communities"
    r1_sub.font.name = "Segoe UI"
    r1_sub.font.size = Pt(17)
    r1_sub.font.bold = True
    r1_sub.font.color.rgb = C_CYAN_ACCENT

    p1_tag = s1_ttf.add_paragraph()
    p1_tag.space_before = Pt(8)
    r1_tag = p1_tag.add_run()
    r1_tag.text = "Making prescriptions understandable, medicines memorable, and healthcare accessible in every Indian language."
    r1_tag.font.name = "Segoe UI"
    r1_tag.font.size = Pt(11)
    r1_tag.font.color.rgb = C_ICE_TEXT

    # Left Bottom Meta Card (Dark Glassmorphic)
    meta_card = add_card(slide1, Inches(0.8), Inches(3.7), Inches(5.8), Inches(3.1), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    mtf = meta_card.text_frame
    mtf.word_wrap = True
    mtf.margin_left = mtf.margin_top = Inches(0.25)
    
    mp1 = mtf.paragraphs[0]
    mr1 = mp1.add_run()
    mr1.text = "TEAM INFORMATION & CONTACT\n"
    mr1.font.bold = True
    mr1.font.size = Pt(11)
    mr1.font.color.rgb = C_CYAN_ACCENT

    meta_items = [
        ("TEAM", "Change_The_World"),
        ("TEAM MEMBER", "Ayush Kumar (Lead Innovator, Class 11th)"),
        ("MENTOR", "Prince Kumar (Technical Mentor & AI Advisor)"),
        ("CONTACT", "kumariafprince@gmail.com"),
        ("GITHUB REPO", "github.com/Prince-git-hub-360/AI-Healthcare-Assistant-for-Rural-Communities")
    ]
    for label, val in meta_items:
        p = mtf.add_paragraph()
        p.space_before = Pt(4)
        rl = p.add_run()
        rl.text = f"{label}: "
        rl.font.bold = True
        rl.font.size = Pt(9.5)
        rl.font.color.rgb = C_SAFFRON
        rv = p.add_run()
        rv.text = val
        rv.font.size = Pt(9.5)
        rv.font.color.rgb = C_WHITE

    # Right Hero Showcase Image / Quote Card
    hero_card = add_card(slide1, Inches(6.9), Inches(0.8), Inches(5.6), Inches(6.0), bg_color=C_CARD_DEEP, border_color=C_BORDER_TEAL)
    # Check if patient dashboard or architecture image exists
    dash_img = os.path.join(SCREENSHOTS_DIR, "figure1_patient_dashboard.png")
    if os.path.exists(dash_img):
        slide1.shapes.add_picture(dash_img, Inches(7.1), Inches(1.1), Inches(5.2), Inches(3.2))

    quote_box = slide1.shapes.add_textbox(Inches(7.1), Inches(4.5), Inches(5.2), Inches(2.1))
    qtf = quote_box.text_frame
    qtf.word_wrap = True
    qp = qtf.paragraphs[0]
    qr = qp.add_run()
    qr.text = "“Understanding the prescription is the first and most critical step toward taking the right medicine at the right time.”\n\n"
    qr.font.italic = True
    qr.font.size = Pt(13)
    qr.font.bold = True
    qr.font.color.rgb = C_WHITE

    qr2 = qp.add_run()
    qr2.text = "Bridging the healthcare literacy barrier for 900M+ rural citizens through vernacular voice AI, visual pillbox routines, and frontline ASHA worker coordination."
    qr2.font.size = Pt(10)
    qr2.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 2: PROBLEM & OPPORTUNITY
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide2, 2, "Problem & Opportunity", "Every patient deserves to understand their own prescription — Closing the last-mile care gap.")

    # 3 Top Core Challenge Cards
    prob_cards = [
        ("01  CAN'T UNDERSTAND", "Prescription Illegibility & Jargon", "Complex medical abbreviations, cursive handwriting, and English terms leave non-literate patients completely unaware of exact dosages and critical precautions."),
        ("02  NEEDS FOLLOW-UP", "Isolated Rural Patient Journey", "When confusion or missed doses occur, rural patients lack immediate clinical guidance and must depend on overburdened frontline ASHA workers."),
        ("03  CAN'T REMEMBER", "Medication Non-Adherence", "Without structured daily timing, meal synchronisation, and vernacular voice alarms, chronic patients inadvertently skip doses or stop therapy prematurely.")
    ]
    for idx, (num_title, sub, body) in enumerate(prob_cards):
        x = Inches(0.8 + idx * 4.0)
        c = add_card(slide2, x, Inches(1.5), Inches(3.7), Inches(2.2), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.18)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = num_title
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_CYAN_ACCENT

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(3)
        r2 = p2.add_run()
        r2.text = sub + "\n"
        r2.font.bold = True
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = C_WHITE

        r3 = p2.add_run()
        r3.text = body
        r3.font.size = Pt(9)
        r3.font.color.rgb = C_ICE_TEXT

    # Bottom Left: Why This Matters (Structured List)
    matters_card = add_card(slide2, Inches(0.8), Inches(3.9), Inches(5.8), Inches(2.9), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    mtf = matters_card.text_frame
    mtf.word_wrap = True
    mtf.margin_left = mtf.margin_top = Inches(0.2)
    
    p = mtf.paragraphs[0]
    r = p.add_run()
    r.text = "WHY THIS MATTERS IN RURAL HEALTHCARE"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_SAFFRON

    matters_list = [
        ("Prescription Confusion: ", "Patients struggle with dose, frequency, duration, and unfamiliar medical abbreviations."),
        ("Language & Literacy: ", "Over 65% of rural citizens cannot read complex English prescription slips."),
        ("Missed Medication: ", "A forgotten dose triggers acute complications, preventable relapses, and hospital readmissions."),
        ("Frontline Workload: ", "10.2 Lakh ASHA workers spend precious hours manually decoding prescriptions during home visits.")
    ]
    for h, b in matters_list:
        p = mtf.add_paragraph()
        p.space_before = Pt(4)
        rh = p.add_run()
        rh.text = f"• {h}"
        rh.font.bold = True
        rh.font.size = Pt(9.5)
        rh.font.color.rgb = C_CYAN_ACCENT
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(9)
        rb.font.color.rgb = C_ICE_TEXT

    # Bottom Right: Scale of Opportunity (3 Data Metrics)
    stats_card = add_card(slide2, Inches(6.8), Inches(3.9), Inches(5.7), Inches(2.9), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN, border_width=1.5)
    stf = stats_card.text_frame
    stf.word_wrap = True
    stf.margin_left = stf.margin_top = Inches(0.2)

    p = stf.paragraphs[0]
    r = p.add_run()
    r.text = "THE SCALE OF THE NATIONAL OPPORTUNITY"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_CYAN_ACCENT

    stats = [
        ("5.86 CRORE", "Hypertension & Diabetes Patients", "Massive chronic patient base requiring continuous, accurate medication adherence (WHO India, 2024)."),
        ("10.2 LAKH", "Active ASHA Workers", "Nationwide last-mile healthcare network ready to be empowered with AI triage tools (NHM India)."),
        ("68% vs 37%", "Adherence with Digital Tracking", "Follow-up rate in ABHA-linked digital programmes vs unassisted paper prescriptions (WHO India).")
    ]
    for stat, label, desc in stats:
        p = stf.add_paragraph()
        p.space_before = Pt(6)
        rs = p.add_run()
        rs.text = f"{stat}  —  "
        rs.font.bold = True
        rs.font.size = Pt(12)
        rs.font.color.rgb = C_SAFFRON
        rl = p.add_run()
        rl.text = f"{label}\n"
        rl.font.bold = True
        rl.font.size = Pt(9.5)
        rl.font.color.rgb = C_WHITE
        rd = p.add_run()
        rd.text = desc
        rd.font.size = Pt(8.5)
        rd.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 3: EXISTING SOLUTIONS & GAP ANALYSIS
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide3, 3, "Existing Solutions & Gap Analysis", "What exists today, where current healthtech falls short, and our core differentiator.")

    # Matrix Table (Dark Theme)
    table_shape = slide3.shapes.add_table(7, 6, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.2))
    table = table_shape.table
    table.columns[0].width = Inches(2.7)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(1.8)
    table.columns[3].width = Inches(1.8)
    table.columns[4].width = Inches(1.8)
    table.columns[5].width = Inches(1.8)

    headers = ["Capability / Feature", "e-Sanjeevani", "Practo / 1mg", "Medisafe", "ASHA (Manual)", "Swasthya Sanchar"]
    for col_idx, htext in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_CARD_DARK if col_idx < 5 else RGBColor(16, 75, 88)
        p = cell.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = htext
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_SAFFRON if col_idx == 5 else C_WHITE

    matrix_data = [
        ("Teleconsult / Clinical Connection", "✓ Full", "✓ Full", "— None", "Limited", "✓ Integrated*"),
        ("Prescription / Health Records", "✓ Digital", "✓ Digital", "— None", "— None", "✓ ABDM Vault"),
        ("Medication Reminders", "— None", "✓ Basic", "✓ App Alerts", "Limited", "✓ Vernacular Audio"),
        ("Plain-Language Explanation", "— None", "— None", "— None", "Limited", "✓ Zero-Literacy AI"),
        ("Voice-First Vernacular Guidance", "— None", "— None", "— None", "Limited", "✓ 12+ Dialects"),
        ("ASHA / Caregiver Follow-Up Loop", "— None", "— None", "— None", "✓ Manual", "✓ Automated Sync")
    ]
    for row_idx, row in enumerate(matrix_data):
        for col_idx, val in enumerate(row):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_BG_DARK if row_idx % 2 == 0 else C_CARD_DARK
            p = cell.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = val
            r.font.size = Pt(9)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = C_WHITE
            elif col_idx == 5:
                r.font.bold = True
                r.font.color.rgb = C_CYAN_ACCENT
            else:
                r.font.color.rgb = C_ICE_TEXT

    # Differentiator Card
    diff_card = add_card(slide3, Inches(0.8), Inches(4.9), Inches(11.7), Inches(0.8), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    dtf = diff_card.text_frame
    dtf.word_wrap = True
    dtf.margin_left = dtf.margin_top = Inches(0.18)
    dp = dtf.paragraphs[0]
    dr_label = dp.add_run()
    dr_label.text = "⭐ OUR CORE DIFFERENTIATOR: "
    dr_label.font.bold = True
    dr_label.font.size = Pt(10.5)
    dr_label.font.color.rgb = C_SAFFRON

    dr_txt = dp.add_run()
    dr_txt.text = "Not another telemedicine app — Swasthya Sanchar AI is a voice-first understanding & adherence layer built around the care and clinical systems that already exist."
    dr_txt.font.size = Pt(10)
    dr_txt.font.color.rgb = C_WHITE

    # Bottom Unmet Need Card
    unmet_card = add_card(slide3, Inches(0.8), Inches(5.85), Inches(11.7), Inches(1.1), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    utf = unmet_card.text_frame
    utf.word_wrap = True
    utf.margin_left = utf.margin_top = Inches(0.18)
    up = utf.paragraphs[0]
    ur1 = up.add_run()
    ur1.text = "THE UNMET NEED WE SOLVE\n"
    ur1.font.bold = True
    ur1.font.size = Pt(10)
    ur1.font.color.rgb = C_CYAN_ACCENT

    ur2 = up.add_run()
    ur2.text = "Most existing health tools solve one isolated fragment: OCR extracts raw text, translation changes words, reminder apps set generic alarms, and telemedicine connects to clinicians. Swasthya Sanchar unites the entire treatment-understanding loop — from prescription capture to plain-language voice explanation, visual adherence pillbox, and frontline ASHA follow-up."
    ur2.font.size = Pt(8.5)
    ur2.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 4: OUR SOLUTION
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide4, 4, "Our Solution: The Treatment Understanding Journey", "From a photograph of a handwritten prescription to a guided vernacular treatment routine.")

    # 6-Step Pipeline Cards Across the Top
    steps = [
        ("1  UPLOAD", "Prescription Scan", "Patient or ASHA worker snaps a photo of the paper prescription."),
        ("2  OCR", "Entity Extraction", "Hybrid OCR extracts medicine names, dosages, frequencies, and durations."),
        ("3  AI PARSING", "Clinical Analysis", "Gemini & Clinical NLP parse drug interactions and verify regimen safety."),
        ("4  SIMPLIFY", "Indic Translation", "Medical jargon converted into simple instructions across 12+ Indian languages."),
        ("5  VOICE & CUES", "Visual Pillbox", "Vernacular audio guidance + morning/meal/night visual routine."),
        ("6  FOLLOW-UP", "ASHA Safety Net", "Missed doses trigger automated caregiver SMS and frontline ASHA alerts.")
    ]
    for idx, (stitle, ssub, sbody) in enumerate(steps):
        x = Inches(0.8 + idx * 1.98)
        c = add_card(slide4, x, Inches(1.5), Inches(1.85), Inches(2.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.12)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = stitle + "\n"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_CYAN_ACCENT

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(2)
        r2 = p2.add_run()
        r2.text = ssub + "\n"
        r2.font.bold = True
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_WHITE

        r3 = p2.add_run()
        r3.text = sbody
        r3.font.size = Pt(7.5)
        r3.font.color.rgb = C_ICE_TEXT

    # 4 Bottom Value Proposition Cards
    vprops = [
        ("01  ZERO-LITERACY BARRIER", "Spoken Vernacular Audio", "Voice guidance in 12+ Indian dialects ensures non-literate and elderly patients never struggle with unreadable text.", C_CYAN_ACCENT),
        ("02  MEDICATION ADHERENCE", "Visual Routine & Pillbox", "Sun/Food/Moon icons turn complex prescriptions into an intuitive, mistake-free daily habit.", C_SAFFRON),
        ("03  HUMAN SAFETY NET", "Frontline ASHA Worker Loop", "Connects patients with local community health workers who receive early alerts when treatment adherence lapses.", C_GREEN),
        ("04  DOCTOR-FRIENDLY SUMMARY", "Dual Output Architecture", "Generates concise clinical summaries and drug contraindication logs for PHC doctors during teleconsults.", C_CYAN_ACCENT)
    ]
    for idx, (vtitle, vsub, vbody, vcol) in enumerate(vprops):
        x = Inches(0.8 + idx * 2.98)
        c = add_card(slide4, x, Inches(4.0), Inches(2.82), Inches(2.2), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.15)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = vtitle + "\n"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = vcol

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(3)
        r2 = p2.add_run()
        r2.text = vsub + "\n"
        r2.font.bold = True
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = C_WHITE

        r3 = p2.add_run()
        r3.text = vbody
        r3.font.size = Pt(8)
        r3.font.color.rgb = C_ICE_TEXT

    # Safety banner
    sbanner = add_card(slide4, Inches(0.8), Inches(6.35), Inches(11.7), Inches(0.55), bg_color=C_CARD_DEEP, border_color=C_BORDER_TEAL)
    sbtf = sbanner.text_frame
    sbp = sbtf.paragraphs[0]
    sbp.margin_left = Inches(0.15)
    sbr = sbp.add_run()
    sbr.text = "🔒 Clinical Safety Guarantee: Swasthya Sanchar AI assists patient comprehension and adherence; clinical diagnoses and prescription decisions strictly remain with qualified healthcare professionals."
    sbr.font.size = Pt(8.5)
    sbr.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 5: TECHNOLOGY & INNOVATION
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide5, 5, "Technology & Architecture", "A Purpose-Fit Multi-Modal AI Stack Built Around the Rural Patient Journey.")

    # Left: Multi-Modal Tech Stack (5 layers)
    tech_card = add_card(slide5, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.4), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    ttf = tech_card.text_frame
    ttf.word_wrap = True
    ttf.margin_left = ttf.margin_top = Inches(0.2)
    
    p = ttf.paragraphs[0]
    r = p.add_run()
    r.text = "TECHNOLOGY STACK & INNOVATION"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_CYAN_ACCENT

    tech_layers = [
        ("1. Frontend & Client Layer", "React 19, Vite, Tailwind CSS, Service Workers", "Accessible, high-contrast, offline-first PWA responsive across low-cost Android smartphones."),
        ("2. Backend & API Services", "Django 5.2 REST Framework, Python 3.12, SQLite / PostgreSQL", "Domain-driven micro-services managing prescription pipelines, ABHA records, and ASHA triage."),
        ("3. AI & Clinical NLP Engine", "Google Gemini 1.5 Flash / Pro + PyTesseract OCR", "Multi-modal vision model trained on medical nomenclature for dosage extraction and contraindication checks."),
        ("4. Vernacular Speech Pipeline", "Whisper STT, Bhashini Indic TTS & Regional Dialect Synthesis", "Bi-directional audio communication supporting 12+ Indian languages (Hindi, Tamil, Telugu, Bhojpuri, etc.)."),
        ("5. Location & Emergency Dispatch", "Leaflet GIS, OpenStreetMap, Geolocation APIs", "Dynamic mapping of nearby PHCs, sub-centres, and 1-tap emergency dispatch escalation.")
    ]
    for h, sub, b in tech_layers:
        p = ttf.add_paragraph()
        p.space_before = Pt(5)
        rh = p.add_run()
        rh.text = f"{h}  "
        rh.font.bold = True
        rh.font.size = Pt(9)
        rh.font.color.rgb = C_SAFFRON

        rsub = p.add_run()
        rsub.text = f"({sub})\n"
        rsub.font.size = Pt(8)
        rsub.font.color.rgb = C_CYAN_ACCENT

        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(8)
        rb.font.color.rgb = C_ICE_TEXT

    # Right: System Architecture Diagram & Data Flow
    arch_card = add_card(slide5, Inches(6.2), Inches(1.5), Inches(6.3), Inches(5.4), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    arch_img = os.path.join(SCREENSHOTS_DIR, "swasthya_sanchar_architecture.png")
    if os.path.exists(arch_img):
        slide5.shapes.add_picture(arch_img, Inches(6.35), Inches(1.65), Inches(6.0), Inches(3.4))
    
    atbox = slide5.shapes.add_textbox(Inches(6.35), Inches(5.2), Inches(6.0), Inches(1.5))
    attf = atbox.text_frame
    attf.word_wrap = True
    ap1 = attf.paragraphs[0]
    ar1 = ap1.add_run()
    ar1.text = "🏛️ END-TO-END DATA FLOW & SECURITY\n"
    ar1.font.bold = True
    ar1.font.size = Pt(10)
    ar1.font.color.rgb = C_CYAN_ACCENT

    ar2 = ap1.add_run()
    ar2.text = "• Client-side encrypted prescription uploads with zero PHI persistence on insecure nodes.\n" \
               "• Asynchronous celery-based OCR & NLP queue for sub-2-second vernacular audio rendering.\n" \
               "• Full compliance with Ayushman Bharat Digital Mission (ABDM) Health Data Management standards."
    ar2.font.size = Pt(8.5)
    ar2.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 6: PROTOTYPE / MVP / DEMONSTRATION
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide6, 6, "Prototype / MVP / Demonstration", "Live Working Demonstration — Functional AI Prescription Extraction & Field Portals.")

    # 3 High Resolution Screenshots Side-by-Side
    demos = [
        ("figure2_prescription_ai.png", "1. AI Prescription & Voice Intelligence", "Scans raw prescription, simplifies medical terms, and provides instant Hindi audio playback."),
        ("figure6_pillbox_view.png", "2. Visual 5-Day Adherence Pillbox", "Morning/Afternoon/Night visual cues replacing text alarms for non-literate patients."),
        ("figure5_asha_dashboard.png", "3. Frontline ASHA Field Dashboard", "Real-time door-to-door triage, vitals tracking, and automated high-risk patient flagging.")
    ]
    for idx, (img_file, dtitle, ddesc) in enumerate(demos):
        x = Inches(0.8 + idx * 4.0)
        c = add_card(slide6, x, Inches(1.5), Inches(3.7), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        
        # Image
        img_path = os.path.join(SCREENSHOTS_DIR, img_file)
        if os.path.exists(img_path):
            slide6.shapes.add_picture(img_path, x + Inches(0.12), Inches(1.65), Inches(3.46), Inches(2.2))

        # Description
        tbox = slide6.shapes.add_textbox(x + Inches(0.12), Inches(3.95), Inches(3.46), Inches(1.7))
        ttf = tbox.text_frame
        ttf.word_wrap = True
        p = ttf.paragraphs[0]
        r = p.add_run()
        r.text = dtitle + "\n"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_CYAN_ACCENT

        p2 = ttf.add_paragraph()
        p2.space_before = Pt(2)
        r2 = p2.add_run()
        r2.text = ddesc
        r2.font.size = Pt(8)
        r2.font.color.rgb = C_ICE_TEXT

    # Bottom MVP Validation Banner
    mvp_card = add_card(slide6, Inches(0.8), Inches(5.95), Inches(11.7), Inches(0.95), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    mtf = mvp_card.text_frame
    mtf.word_wrap = True
    mtf.margin_left = mtf.margin_top = Inches(0.15)
    mp = mtf.paragraphs[0]
    mr = mp.add_run()
    mr.text = "🏆 WHAT THE PROTOTYPE PROVES (100% FUNCTIONAL CODEBASE):\n"
    mr.font.bold = True
    mr.font.size = Pt(9.5)
    mr.font.color.rgb = C_SAFFRON

    mr2 = mp.add_run()
    mr2.text = "✓ Live Multimodal OCR extracts handwritten dosages in <3.0 seconds.\n" \
               "✓ Vernacular TTS generates natural, culturally resonant spoken audio in Hindi, Tamil & Telugu.\n" \
               "✓ Offline PWA storage syncs health records and vitals seamlessly during connectivity dropouts."
    mr2.font.size = Pt(8.5)
    mr2.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 7: TARGET USERS & USE CASES
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide7, 7, "Target Users & Real-World Use Cases", "Engineered around the people who deliver and receive care at the last mile.")

    # 3 User Segment Cards
    users = [
        ("👤 RURAL PATIENTS & ELDERLY", "Primary Care Beneficiaries", "900M+ citizens facing literacy and dialect barriers.", [
            "Voice-first guidance in their native dialect.",
            "Visual pillbox with Sun/Meal/Moon cues.",
            "1-tap SOS emergency assistance."
        ], C_CYAN_ACCENT),
        ("👩‍⚕️ ASHA & FRONTLINE WORKERS", "Community Health Safety Net", "10.2 Lakh frontline workers across Indian villages.", [
            "Door-to-door offline health triage.",
            "Automated high-risk maternal/NCD alerts.",
            "Rapid ABHA card creation and management."
        ], C_SAFFRON),
        ("👨‍⚕️ PHC & TELEMEDICINE DOCTORS", "Clinical Decision Makers", "Overburdened rural medical officers & teleconsultants.", [
            "Structured prescription summaries.",
            "Drug-drug interaction safety checks.",
            "Pre-triaged patient histories saving 50% time."
        ], C_GREEN)
    ]
    for idx, (utitle, usub, uaud, ufeats, ucol) in enumerate(users):
        x = Inches(0.8 + idx * 4.0)
        c = add_card(slide7, x, Inches(1.5), Inches(3.7), Inches(2.7), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.18)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = utitle + "\n"
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = ucol

        p_sub = ctf.add_paragraph()
        p_sub.space_before = Pt(2)
        r_sub = p_sub.add_run()
        r_sub.text = f"{usub}  •  {uaud}\n"
        r_sub.font.bold = True
        r_sub.font.size = Pt(8.5)
        r_sub.font.color.rgb = C_WHITE

        for f in ufeats:
            pf = ctf.add_paragraph()
            pf.space_before = Pt(3)
            rf = pf.add_run()
            rf.text = f"✓ {f}"
            rf.font.size = Pt(8.5)
            rf.font.color.rgb = C_ICE_TEXT

    # 4 Real-World Use Case Cards (Bottom)
    use_cases = [
        ("01  Prescription Understanding", "Patient uploads a photo of a messy prescription slip and receives clear spoken dosage guidance in Bhojpuri/Hindi within seconds."),
        ("02  Missed-Dose Escalation", "Elderly patient misses an afternoon hypertension tablet; system notifies family caregiver via WhatsApp/SMS and queues ASHA follow-up."),
        ("03  Tele-Consultation Triage", "PHC doctor receives an AI-extracted clinical timeline and drug interaction check prior to starting a 3-minute video consultation."),
        ("04  Chronic Disease Management", "Diabetic patient adheres to a 30-day insulin routine through daily morning audio reminders and visual color-coded pillbox cues.")
    ]
    for idx, (uc_title, uc_desc) in enumerate(use_cases):
        x = Inches(0.8 + idx * 2.98)
        c = add_card(slide7, x, Inches(4.4), Inches(2.82), Inches(2.5), bg_color=C_CARD_DEEP, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.15)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = uc_title + "\n"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_CYAN_ACCENT

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(4)
        r2 = p2.add_run()
        r2.text = uc_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 8: IMPACT & MEASURABLE OUTCOMES
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide8, 8, "Impact & Measurable Outcomes", "Quantifying real change in adherence, clinical efficiency, and health equity.")

    # 4 Big Quantified Impact Cards
    impact_metrics = [
        ("≈ 50%", "Doctor Triage Time Saved", "Pre-structured digital timelines allow rural PHC doctors to review cases in 2 minutes instead of 5.", C_CYAN_ACCENT),
        ("100%", "Zero-Literacy Voice Pathway", "Complete spoken vernacular journey removing reading barriers for non-literate patients.", C_SAFFRON),
        ("12+", "Regional Indian Languages", "Direct vernacular support across Hindi, Tamil, Telugu, Bengali, Marathi, Bhojpuri, and more.", C_GREEN),
        ("≥ 75%", "Medication Adherence Rate", "Target adherence rate in pilot cohorts through daily vernacular audio & visual pillbox cues.", C_CYAN_ACCENT)
    ]
    for idx, (num, label, desc, col) in enumerate(impact_metrics):
        x = Inches(0.8 + idx * 2.98)
        c = add_card(slide8, x, Inches(1.5), Inches(2.82), Inches(3.0), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.18)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = num + "\n"
        r.font.bold = True
        r.font.size = Pt(30)
        r.font.color.rgb = col

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(3)
        r2 = p2.add_run()
        r2.text = label + "\n\n"
        r2.font.bold = True
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = C_WHITE

        r3 = p2.add_run()
        r3.text = desc
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = C_ICE_TEXT

    # Bottom SDG Alignment & Impact Logic
    sdg_card = add_card(slide8, Inches(0.8), Inches(4.7), Inches(11.7), Inches(2.2), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    stf = sdg_card.text_frame
    stf.word_wrap = True
    stf.margin_left = stf.margin_top = Inches(0.2)
    
    p = stf.paragraphs[0]
    r = p.add_run()
    r.text = "GLOBAL SUSTAINABLE DEVELOPMENT GOALS (SDG) ALIGNMENT\n"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_SAFFRON

    sdgs = [
        ("SDG 3: Good Health & Well-Being", "Dramatically reduces avoidable medication mistakes, secondary hospitalizations, and maternal health complications in remote villages."),
        ("SDG 10: Reduced Inequalities", "Democratizes high-end multi-modal AI for rural and economically vulnerable citizens who do not speak English or own expensive computers."),
        ("National Health Mission (NHM) & Bharat 2047", "Empowers 1.4M frontline workers with automated screening tools, accelerating universal digital health coverage.")
    ]
    for s_title, s_desc in sdgs:
        p = stf.add_paragraph()
        p.space_before = Pt(3)
        rs = p.add_run()
        rs.text = f"• {s_title}: "
        rs.font.bold = True
        rs.font.size = Pt(9.5)
        rs.font.color.rgb = C_CYAN_ACCENT
        rd = p.add_run()
        rd.text = s_desc
        rd.font.size = Pt(9)
        rd.font.color.rgb = C_ICE_TEXT

    # =========================================================================
    # SLIDE 9: BUSINESS MODEL & IMPLEMENTATION ROADMAP
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide9, 9, "Business Model & Implementation Roadmap", "A Government-Compatible & Sustainable Path from Village Pilot to National Scale.")

    # Left: Sustainability Model (3 Cards)
    left_card = add_card(slide9, Inches(0.8), Inches(1.5), Inches(5.4), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    ltf = left_card.text_frame
    ltf.word_wrap = True
    ltf.margin_left = ltf.margin_top = Inches(0.2)
    
    p = ltf.paragraphs[0]
    r = p.add_run()
    r.text = "SUSTAINABILITY & REVENUE MODEL"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_CYAN_ACCENT

    models = [
        ("1. B2G & National Health Mission (NHM)", "Integration with state health departments and Ayushman Bharat Health & Wellness Centres (AB-HWCs) as public infrastructure."),
        ("2. CSR & Public Health Grants", "Targeting ICMR, Grand Challenges India, and healthtech innovation funds to support multi-district validation and language expansion."),
        ("3. NGO & Community Health Outreach", "Partnerships with rural health NGOs (e.g., SEWA, Piramal Swasthya) for community-level deployment and ASHA training.")
    ]
    for mtitle, mdesc in models:
        p = ltf.add_paragraph()
        p.space_before = Pt(6)
        rm = p.add_run()
        rm.text = f"{mtitle}\n"
        rm.font.bold = True
        rm.font.size = Pt(9.5)
        rm.font.color.rgb = C_SAFFRON
        rd = p.add_run()
        rd.text = mdesc
        rd.font.size = Pt(8.5)
        rd.font.color.rgb = C_ICE_TEXT

    # Right: 3-Phase Deployment Roadmap
    right_card = add_card(slide9, Inches(6.4), Inches(1.5), Inches(6.1), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    rtf = right_card.text_frame
    rtf.word_wrap = True
    rtf.margin_left = rtf.margin_top = Inches(0.2)
    
    p = rtf.paragraphs[0]
    r = p.add_run()
    r.text = "PHASED DEPLOYMENT ROADMAP"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_CYAN_ACCENT

    phases = [
        ("PHASE 1: DISTRICT PILOT (Months 1–6)", "10–20 ASHA workers in 1 rural district. Measure baseline comprehension, adherence compliance, and triage time savings across 1,000 patients."),
        ("PHASE 2: STATE INTEGRATION (Months 7–12)", "Connect with state telemedicine portals and e-Sanjeevani API pathways. Expand to 50+ Primary Health Centres with 6 Indian languages."),
        ("PHASE 3: MULTI-STATE SCALE (Months 13–24)", "Roll out across 10,000+ village wellness centres, introducing on-device offline edge AI and complete ABDM health record exchange.")
    ]
    for ptitle, pdesc in phases:
        p = rtf.add_paragraph()
        p.space_before = Pt(6)
        rp = p.add_run()
        rp.text = f"{ptitle}\n"
        rp.font.bold = True
        rp.font.size = Pt(9.5)
        rp.font.color.rgb = C_GREEN
        rd = p.add_run()
        rd.text = pdesc
        rd.font.size = Pt(8.5)
        rd.font.color.rgb = C_ICE_TEXT

    # Bottom Governance Banner
    gov_card = add_card(slide9, Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.9), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    gtf = gov_card.text_frame
    gtf.word_wrap = True
    gtf.margin_left = gtf.margin_top = Inches(0.15)
    gp = gtf.paragraphs[0]
    gr1 = gp.add_run()
    gr1.text = "🛡️ ETHICAL GOVERNANCE & DATA PRIVACY PRINCIPLES\n"
    gr1.font.bold = True
    gr1.font.size = Pt(9.5)
    gr1.font.color.rgb = C_SAFFRON

    gr2 = gp.add_run()
    gr2.text = "Explicit Patient Consent  •  Minimal Data Collection  •  Role-Based Access Control  •  End-to-End Encryption  •  Human-in-the-Loop Clinical Fallback"
    gr2.font.size = Pt(8.5)
    gr2.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 10: FEASIBILITY & SCALABILITY
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide10, 10, "Feasibility & Scalability", "Engineering resilience for low-resource environments without compromising clinical trust.")

    # 3 Pillars of Feasibility
    feas = [
        ("1. TECHNICAL FEASIBILITY", "Lightweight & Resilient Architecture", [
            "Lightweight REST APIs (<150ms response latency).",
            "Responsive PWA optimized for ₹6,000 Android phones.",
            "Local SQLite/IndexedDB caching for zero-network villages.",
            "Modular AI orchestration decoupling OCR from translation."
        ], C_CYAN_ACCENT),
        ("2. OPERATIONAL & RISK CONTROL", "Clinical Safety & Human Oversight", [
            "AI outputs are assistive; doctors retain clinical authority.",
            "Automatic confidence thresholding flags blurry slips.",
            "Role-based access separating ASHA and patient views.",
            "Emergency SOS bypass for critical red-flag symptoms."
        ], C_SAFFRON),
        ("3. HORIZONTAL SCALABILITY", "Multi-State Elastic Infrastructure", [
            "Stateless micro-services scale OCR & TTS independently.",
            "Queue-based asynchronous workers handle peak loads.",
            "Extensible language dictionary supports new regional dialects.",
            "Zero proprietary hardware required for field deployment."
        ], C_GREEN)
    ]
    for idx, (ftitle, fsub, fitems, fcol) in enumerate(feas):
        x = Inches(0.8 + idx * 4.0)
        c = add_card(slide10, x, Inches(1.5), Inches(3.7), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.18)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = ftitle + "\n"
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = fcol

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(2)
        r2 = p2.add_run()
        r2.text = fsub + "\n\n"
        r2.font.bold = True
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = C_WHITE

        for it in fitems:
            pit = ctf.add_paragraph()
            pit.space_before = Pt(3)
            rit = pit.add_run()
            rit.text = f"✓ {it}"
            rit.font.size = Pt(8.5)
            rit.font.color.rgb = C_ICE_TEXT

    # Bottom Scaling Principle Card
    scale_card = add_card(slide10, Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.9), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    stf = scale_card.text_frame
    stf.word_wrap = True
    stf.margin_left = stf.margin_top = Inches(0.15)
    sp = stf.paragraphs[0]
    sr1 = sp.add_run()
    sr1.text = "💡 CORE SCALING PRINCIPLE: SCALE THE CARE WORKFLOW, NOT JUST THE AI\n"
    sr1.font.bold = True
    sr1.font.size = Pt(9.5)
    sr1.font.color.rgb = C_CYAN_ACCENT

    sr2 = sp.add_run()
    sr2.text = "The product remains completely reliable and useful even if network connectivity drops, language models fluctuate, or an ASHA worker needs to take manual control of patient records."
    sr2.font.size = Pt(8.5)
    sr2.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 11: COMPETITIVE ADVANTAGE
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide11, 11, "Competitive Advantage & USP", "Why Swasthya Sanchar Wins the Last Mile & Outperforms Conventional Solutions.")

    # 3 Core Differentiators Across the Top
    d_cards = [
        ("VOICE-FIRST AI", "Zero-Literacy Barrier", "Patients hear spoken instructions in their native village dialect without needing to read complex scripts."),
        ("DUAL CLINICAL OUTPUT", "Patient + Doctor Synergy", "Delivers ultra-simplified instructions for patients while generating structured clinical logs for PHC doctors."),
        ("COMMUNITY-CENTRIC", "Frontline ASHA Worker Loop", "Binds patient, family caregiver, and ASHA worker into a proactive treatment adherence safety net.")
    ]
    for idx, (dtitle, dsub, dbody) in enumerate(d_cards):
        x = Inches(0.8 + idx * 4.0)
        c = add_card(slide11, x, Inches(1.5), Inches(3.7), Inches(1.8), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = Inches(0.15)
        
        p = ctf.paragraphs[0]
        r = p.add_run()
        r.text = dtitle + "\n"
        r.font.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = C_CYAN_ACCENT

        p2 = ctf.add_paragraph()
        p2.space_before = Pt(2)
        r2 = p2.add_run()
        r2.text = dsub + "\n"
        r2.font.bold = True
        r2.font.size = Pt(9)
        r2.font.color.rgb = C_WHITE

        r3 = p2.add_run()
        r3.text = dbody
        r3.font.size = Pt(8)
        r3.font.color.rgb = C_ICE_TEXT

    # Competitive Advantage Matrix Table (Dark Theme)
    t_shape11 = slide11.shapes.add_table(6, 5, Inches(0.8), Inches(3.45), Inches(11.7), Inches(2.5))
    table11 = t_shape11.table
    table11.columns[0].width = Inches(3.3)
    table11.columns[1].width = Inches(2.1)
    table11.columns[2].width = Inches(2.1)
    table11.columns[3].width = Inches(2.1)
    table11.columns[4].width = Inches(2.1)

    t11_headers = ["Key Capability", "Generic Health Apps", "Stand-Alone OCR", "Standard Reminder Apps", "Swasthya Sanchar AI"]
    for col_idx, htext in enumerate(t11_headers):
        cell = table11.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_CARD_DARK if col_idx < 4 else RGBColor(16, 75, 88)
        p = cell.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = htext
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = C_SAFFRON if col_idx == 4 else C_WHITE

    t11_rows = [
        ("Voice-First Native Dialect Audio", "Limited", "— None", "Limited", "✓ Full (12+ Dialects)"),
        ("Prescription Vision-to-Voice in <3s", "Limited", "✓ Raw OCR Only", "— None", "✓ Multi-Modal AI"),
        ("Visual 5-Day Meal-Synced Pillbox", "Limited", "— None", "✓ Text Alarms", "✓ Sun / Meal / Moon"),
        ("Frontline ASHA & Caregiver Loop", "Rare", "— None", "— None", "✓ Automated SMS/Sync"),
        ("Doctor EHR Clinical Summary", "Rare", "— None", "— None", "✓ ABDM Structured")
    ]
    for row_idx, row in enumerate(t11_rows):
        for col_idx, val in enumerate(row):
            cell = table11.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_BG_DARK if row_idx % 2 == 0 else C_CARD_DARK
            p = cell.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = val
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = C_WHITE
            elif col_idx == 4:
                r.font.bold = True
                r.font.color.rgb = C_CYAN_ACCENT
            else:
                r.font.color.rgb = C_ICE_TEXT

    # Positioning Callout
    pos_card = add_card(slide11, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.75), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN)
    ptf = pos_card.text_frame
    ptf.word_wrap = True
    ptf.margin_left = ptf.margin_top = Inches(0.12)
    pp = ptf.paragraphs[0]
    pr = pp.add_run()
    pr.text = "🎯 STRATEGIC POSITIONING: "
    pr.font.bold = True
    pr.font.size = Pt(9.5)
    pr.font.color.rgb = C_SAFFRON

    pr2 = pp.add_run()
    pr2.text = "We are not trying to replace doctors or compete with government telemedicine. We are building the indispensable communication and adherence layer that ensures every rural citizen understands and follows what the doctor already prescribed."
    pr2.font.size = Pt(8.5)
    pr2.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 12: TEAM & VISION
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_dark_header(slide12, 12, "Team & Vision", "Because understanding medical treatment should be a fundamental human right, not a privilege.")

    # Left: Team Cards (Ayush + Prince)
    team_card = add_card(slide12, Inches(0.8), Inches(1.5), Inches(5.6), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    tttf = team_card.text_frame
    tttf.word_wrap = True
    tttf.margin_left = tttf.margin_top = Inches(0.2)
    
    tp = tttf.paragraphs[0]
    tr = tp.add_run()
    tr.text = "THE INNOVATORS & ROLES"
    tr.font.bold = True
    tr.font.size = Pt(11)
    tr.font.color.rgb = C_CYAN_ACCENT

    members = [
        ("AYUSH KUMAR", "Lead AI Developer & Fullstack Architect (Class 11th, NIOS)", [
            "Architected Django 5.2 backend, React 19 UI, and PWA offline storage.",
            "Engineered multi-modal OCR pipeline and Bhashini vernacular TTS engine.",
            "Designed low-literacy visual pillbox and ASHA triage workflows."
        ]),
        ("PRINCE KUMAR", "Technical Mentor & AI HealthTech Advisor", [
            "Guided domain-driven clinical system architecture and security.",
            "Advised on Ayushman Bharat (ABDM) data standards & HIPAA alignment.",
            "Supervised edge AI optimization and integration test suites."
        ])
    ]
    for name, role, duties in members:
        p = tttf.add_paragraph()
        p.space_before = Pt(5)
        rn = p.add_run()
        rn.text = f"👨‍💻 {name}  —  "
        rn.font.bold = True
        rn.font.size = Pt(9.5)
        rn.font.color.rgb = C_SAFFRON
        rr = p.add_run()
        rr.text = f"{role}\n"
        rr.font.size = Pt(8.5)
        rr.font.color.rgb = C_WHITE
        for d in duties:
            pd = tttf.add_paragraph()
            pd.space_before = Pt(1)
            rd = pd.add_run()
            rd.text = f"• {d}"
            rd.font.size = Pt(8)
            rd.font.color.rgb = C_ICE_TEXT

    # Right: Future Vision (4 Items)
    vis_card = add_card(slide12, Inches(6.6), Inches(1.5), Inches(5.9), Inches(4.3), bg_color=C_CARD_DARK, border_color=C_BORDER_TEAL)
    vtf = vis_card.text_frame
    vtf.word_wrap = True
    vtf.margin_left = vtf.margin_top = Inches(0.2)
    
    vp = vtf.paragraphs[0]
    vr = vp.add_run()
    vr.text = "FUTURE VISION: BHARAT HEALTHCARE 2047"
    vr.font.bold = True
    vr.font.size = Pt(11)
    vr.font.color.rgb = C_CYAN_ACCENT

    vis_items = [
        ("1. On-Device Edge AI Models: ", "Running ultra-compact quantized vision models locally on low-cost smartphones without internet."),
        ("2. IoT Smart Pillbox & Wearable Sync: ", "Hardware sensors detecting pill removal and synchronizing vitals for elderly and chronic cardiac patients."),
        ("3. Automated 108 Emergency SOS: ", "Direct API dispatch to local 108 ambulance networks upon detecting severe drug reactions or acute vitals."),
        ("4. National ABDM Health Locker Sync: ", "Instant bidirectional synchronization with Ayushman Bharat digital health vaults across all 28 Indian states.")
    ]
    for vh, vb in vis_items:
        p = vtf.add_paragraph()
        p.space_before = Pt(4)
        rvh = p.add_run()
        rvh.text = vh
        rvh.font.bold = True
        rvh.font.size = Pt(9)
        rvh.font.color.rgb = C_GREEN
        rvb = p.add_run()
        rvb.text = vb
        rvb.font.size = Pt(8.5)
        rvb.font.color.rgb = C_ICE_TEXT

    # Bottom The Ask & Contact Details (High Contrast Box)
    ask_card = add_card(slide12, Inches(0.8), Inches(5.95), Inches(11.7), Inches(1.05), bg_color=C_CARD_DEEP, border_color=C_BORDER_CYAN, border_width=1.5)
    atf = ask_card.text_frame
    atf.word_wrap = True
    atf.margin_left = atf.margin_top = Inches(0.15)
    ap = atf.paragraphs[0]
    ar1 = ap.add_run()
    ar1.text = "🤝 THE ASK & CALL TO ACTION: "
    ar1.font.bold = True
    ar1.font.size = Pt(9.5)
    ar1.font.color.rgb = C_SAFFRON

    ar2 = ap.add_run()
    ar2.text = "Pilot Swasthya Sanchar AI with frontline health workers, validate clinical adherence outcomes, and partner to build a responsible vernacular healthcare layer for rural India.\n"
    ar2.font.size = Pt(9)
    ar2.font.color.rgb = C_WHITE

    p_contact = atf.add_paragraph()
    p_contact.space_before = Pt(2)
    rc1 = p_contact.add_run()
    rc1.text = "GitHub: "
    rc1.font.bold = True
    rc1.font.size = Pt(8.5)
    rc1.font.color.rgb = C_CYAN_ACCENT

    rc2 = p_contact.add_run()
    rc2.text = "github.com/Prince-git-hub-360/AI-Healthcare-Assistant-for-Rural-Communities  •  "
    rc2.font.size = Pt(8.5)
    rc2.font.color.rgb = C_ICE_TEXT

    rc3 = p_contact.add_run()
    rc3.text = "Email: "
    rc3.font.bold = True
    rc3.font.size = Pt(8.5)
    rc3.font.color.rgb = C_CYAN_ACCENT

    rc4 = p_contact.add_run()
    rc4.text = "kumariafprince@gmail.com  •  Phone: +91 9008802105"
    rc4.font.size = Pt(8.5)
    rc4.font.color.rgb = C_ICE_TEXT

    prs.save(pptx_path)
    print(f"[SUCCESS] High-fidelity Dark Teal PPTX saved at: {pptx_path}")

if __name__ == "__main__":
    out_file = "ChangeTheWorld_SwasthyaSancharAI_NIOS.pptx"
    build_perfect_presentation(out_file)
