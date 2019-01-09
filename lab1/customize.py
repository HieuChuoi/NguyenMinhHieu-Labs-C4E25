sickness_list = ["thương hàn", "kiết lị", "ebola"]

html = '''   #template
<p>Ch&agrave;o sếp.</p>
<p>S&aacute;ng nay ngủ dậy em cảm thấy <strong>đau bụng</strong>, b&aacute;c sỹ bảo em bị <span style="text-decoration: underline;">{{sickness}}</span>. Sếp cho em nghỉ l&agrave;m h&ocirc;m nay nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-embarassed.gif" alt="embarassed" /></p>
<p>Em cảm ơn sếp.</p>
<p>Nh&acirc;n vi&ecirc;n</p>
'''

from random import choice
html_content = html.replace("{{sickness}}", choice(sickness_list))   #content

from gmail import GMail, Message
gmail = GMail('nguyenminhhieu2508@gmail.com','nguyenminhhieu')
msg = Message('text',to='qhuydtvt@gmail.com',html=html_content)
gmail.send(msg)