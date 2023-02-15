import pypdf

html = """
<style type="text/css">
    table.tbl {border-width: 1px; border-style: solid; border-color:#101010;  color: black;}";
</style>

    <div align=right>  Test </div>
    <div align=left style="font-size: 14pt; ">
       ADVACAM <br>
       U Pergamenky 12<br>
       Prague
    </div>

    <h1 align=center>DOCUMENT TITLE</h1>
    <p align=justify>
       document content document content document content document content document content document content document content document content document content document content 
       document content document content document content document content document content document content document content document content document content document content 
    </p>
    <div align=right>sincerly</div>

    <p style="page-break-before:always;"></p>
    New Page<br>
"""

pypdf.createPdfFromHtml("test.pdf", html)
