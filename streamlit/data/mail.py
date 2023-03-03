from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from dotenv import load_dotenv
import os


mensaje = MIMEMultipart("plain")
mensaje["From"] = "luism88@gmail.com"
mensaje["To"] = "luism88@gmail.com"
mensaje["Subject"] = "Correo de prueba Python"
adjunto = MIMEBase("aplication","octect-stream")
adjunto.set_payload(open("archivo.pdf","rb").read())
adjunto.add_header("content-Disposition", 'attchment;filename = "mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login("correo_de_envio:os.getenv("URL")"","contraseña:os.getenv('URL')")
smtp.sendmail("luism88@gmail.com","luism88@gmail.com",mensaje.as_string)
smtp.quit()

