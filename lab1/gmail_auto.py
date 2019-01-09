from gmail import GMail, Message
gmail = GMail('nguyenminhhieu2508@gmail.com','nguyenminhhieu')
msg = Message('text',to='qhuydtvt@gmail.com',html='''<p>Ch&agrave;o sếp.</p>
<p>S&aacute;ng nay ngủ dậy em cảm thấy <strong>đau bụng</strong>, b&aacute;c sỹ bảo em bị <span style="text-decoration: underline;">kiết lỵ</span>. Sếp cho em nghỉ l&agrave;m h&ocirc;m nay nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-embarassed.gif" alt="embarassed" /></p>
<p>Em cảm ơn sếp.</p>
<p>Nh&acirc;n vi&ecirc;n</p>''')
gmail.send(msg)