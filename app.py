import streamlit as st
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Gerador de Código de Barras e QR Code", layout="centered")

st.title("📦 Gerador de Código de Barras e QR Code")
st.write("Insira um valor para gerar os códigos:")

# Campo de entrada do usuário
valor_input = st.text_input("Digite o valor:", placeholder="Ex: 1234567890")

if valor_input:
    # Geração do QR Code
    qr = qrcode.make(valor_input)
    
    # Salvar QR Code em memória
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    
    # Geração do Código de Barras (Code128)
    codigo_barras_io = BytesIO()
    barcode = Code128(valor_input, writer=ImageWriter())
    barcode.write(codigo_barras_io)
    
    # Converter bytes para imagens PIL
    img_qr = Image.open(qr_io)
    img_barcode = Image.open(codigo_barras_io)

    # Exibir as imagens
    st.subheader("✅ QR Code:")
    st.image(img_qr, caption="QR Code", use_column_width=True)

    st.subheader("📊 Código de Barras (Code128):")
    st.image(img_barcode, caption="Código de Barras", use_column_width=True)

    # Botões para download
    st.download_button(
        label="📥 Baixar QR Code",
        data=qr_io.getvalue(),
        file_name="qrcode.png",
        mime="image/png"
    )

    st.download_button(
        label="📥 Baixar Código de Barras",
        data=codigo_barras_io.getvalue(),
        file_name="codigo_barras.png",
        mime="image/png"
    )
else:
    st.info("Por favor, insira um valor para gerar os códigos.")