import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_monograph():
    doc = Document()

    # Section Margins
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

        # Header
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr1 = hp.add_run("UNLEASH LLM National Finalist & Master Research Monograph  |  ")
        hr1.font.name = "Calibri"
        hr1.font.size = Pt(8.5)
        hr1.font.color.rgb = RGBColor(100, 116, 139)
        hr2 = hp.add_run("Swasthya Sanchar AI")
        hr2.font.name = "Calibri"
        hr2.font.size = Pt(9)
        hr2.font.bold = True
        hr2.font.color.rgb = RGBColor(0, 86, 145)

        # Footer
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        fr_left = fp.add_run("AI-Powered Healthcare Communication Assistant for Rural Communities  •  Comprehensive Research Publication\t")
        fr_left.font.name = "Calibri"
        fr_left.font.size = Pt(8.5)
        fr_left.font.color.rgb = RGBColor(148, 163, 184)

        r_page = fp.add_run("Page ")
        r_page.font.name = "Calibri"
        r_page.font.size = Pt(8.5)
        r_page.font.color.rgb = RGBColor(100, 116, 139)
        fld1 = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        fp._p.append(fld1)

        r_of = fp.add_run(" of ")
        r_of.font.name = "Calibri"
        r_of.font.size = Pt(8.5)
        r_of.font.color.rgb = RGBColor(100, 116, 139)
        fld2 = parse_xml(r'<w:fldSimple %s w:instr="NUMPAGES"/>' % nsdecls('w'))
        fp._p.append(fld2)

    # Color Palette
    NAVY = RGBColor(0, 86, 145)       # Primary #005691
    BLUE = RGBColor(2, 132, 199)      # Tech #0284C7
    CHARCOAL = RGBColor(30, 41, 59)   # Body #1E293B
    MUTED = RGBColor(100, 116, 139)   # #64748B

    def add_p(text, bold_prefix=None, space_after=6, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Calibri"
            rb.font.size = Pt(10)
            rb.font.bold = True
            rb.font.color.rgb = CHARCOAL
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.italic = italic
        r.font.color.rgb = CHARCOAL
        return p

    def add_h1(num_str, title_str):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(f"CHAPTER {num_str}: {title_str.upper()}")
        r.font.name = "Arial"
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = NAVY
        return h

    def add_h2(num_str, title_str):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(f"{num_str} {title_str}")
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = BLUE
        return h

    def add_h3(num_str, title_str):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(f"{num_str} {title_str}")
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = NAVY
        return h

    def add_callout(text, title="RESEARCH HIGHLIGHT"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl, color="0284C7", sz="12", val="left")
        c = tbl.rows[0].cells[0]
        c.width = Inches(6.9)
        set_cell_background(c, "F0F9FF")
        set_cell_margins(c, top=80, bottom=80, left=130, right=130)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        rt = p.add_run(f"📌 {title}: ")
        rt.font.name = "Calibri"
        rt.font.size = Pt(9.5)
        rt.font.bold = True
        rt.font.color.rgb = NAVY
        rc = p.add_run(text)
        rc.font.name = "Calibri"
        rc.font.size = Pt(9)
        rc.font.color.rgb = CHARCOAL
        p_post = doc.add_paragraph()
        p_post.paragraph_format.space_after = Pt(4)

    def add_algorithm_box(alg_num, alg_title, input_desc, output_desc, steps):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl, color="005691", sz="8")
        c = tbl.rows[0].cells[0]
        c.width = Inches(6.9)
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=80, bottom=80, left=130, right=130)
        
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(3)
        rt = p.add_run(f"ALGORITHM {alg_num}: {alg_title.upper()}\n")
        rt.font.name = "Courier New"
        rt.font.size = Pt(9.5)
        rt.font.bold = True
        rt.font.color.rgb = NAVY

        p.add_run(f"INPUT:  {input_desc}\nOUTPUT: {output_desc}\n").font.name = "Courier New"
        p.runs[-1].font.size = Pt(8.5)
        p.runs[-1].font.bold = True
        p.runs[-1].font.color.rgb = MUTED

        p.add_run("━" * 58 + "\n").font.color.rgb = RGBColor(203, 213, 225)
        for idx, step in enumerate(steps, 1):
            rs = p.add_run(f"{idx:02d}: {step}\n")
            rs.font.name = "Courier New"
            rs.font.size = Pt(8.5)
            rs.font.color.rgb = CHARCOAL

        p_end = doc.add_paragraph()
        p_end.paragraph_format.space_after = Pt(4)

    def add_equation_box(eq_title, eq_latex, explanation):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl, color="CBD5E1", sz="4")
        c = tbl.rows[0].cells[0]
        c.width = Inches(6.9)
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=70, bottom=70, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        r0 = p.add_run(f"Mathematical Formulation — {eq_title}\n")
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = NAVY

        r_eq = p.add_run(f"   {eq_latex}\n")
        r_eq.font.name = "Courier New"
        r_eq.font.size = Pt(10)
        r_eq.font.bold = True
        r_eq.font.color.rgb = BLUE

        r_exp = p.add_run(f"Where: {explanation}")
        r_exp.font.name = "Calibri"
        r_exp.font.size = Pt(8.5)
        r_exp.font.italic = True
        r_exp.font.color.rgb = MUTED

        p_post = doc.add_paragraph()
        p_post.paragraph_format.space_after = Pt(4)

    def add_image_safe(img_path, caption, width=Inches(6.2)):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.add_run().add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            rc = p_cap.add_run(f"Caption: {caption}")
            rc.font.name = "Calibri"
            rc.font.size = Pt(8.5)
            rc.font.bold = True
            rc.font.color.rgb = MUTED

    print("Building full 35-page master thesis...")

    # Load and execute generator script logic
    # To ensure robust execution, let's write out the full rich text structure
    return doc

print("Script template ready.")
