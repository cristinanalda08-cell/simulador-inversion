import streamlit as st

# Configuración estética
st.set_page_config(page_title="Simulador VAN y Payback", page_icon="💰")

st.title("📊 Simulador de Inversiones")
st.write("Herramienta interactiva para el análisis de proyectos de inversión.")

# Formulario de entrada
with st.form("datos_proyecto"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Nombre del Proyecto", "Mi Proyecto")
        inversion = st.number_input("Inversión Inicial (€)", min_value=0.0, value=1000.0)
    with col_b:
        tasa = st.number_input("Tasa de descuento % (k)", min_value=0.0, value=5.0) / 100
    
    st.write("---")
    st.subheader("Flujos de Caja (Años 1 al 10)")
    
    # Creamos 10 casillas para los flujos
    c1, c2, c3, c4, c5 = st.columns(5)
    f1 = c1.number_input("Año 1", value=0.0)
    f2 = c2.number_input("Año 2", value=0.0)
    f3 = c3.number_input("Año 3", value=0.0)
    f4 = c4.number_input("Año 4", value=0.0)
    f5 = c5.number_input("Año 5", value=0.0)
    
    c6, c7, c8, c9, c10 = st.columns(5)
    f6 = c6.number_input("Año 6", value=0.0)
    f7 = c7.number_input("Año 7", value=0.0)
    f8 = c8.number_input("Año 8", value=0.0)
    f9 = c9.number_input("Año 9", value=0.0)
    f10 = c10.number_input("Año 10", value=0.0)
    
    submitted = st.form_submit_button("Calcular Proyecto")

if submitted:
    flujos = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    
    # CÁLCULO VAN
    van = -inversion
    for i, f in enumerate(flujos):
        van += f / (1 + tasa)**(i+1)
        
    # CÁLCULO PAYBACK
    acumulado = -inversion
    payback_resultado = "No se recupera"
    for i, f in enumerate(flujos):
        anterior = acumulado
        acumulado += f
        if acumulado >= 0 and f > 0:
            anio_recup = i + (abs(anterior) / f)
            payback_resultado = f"{anio_recup:.2f} años"
            break
            
    # MOSTRAR RESULTADOS
    st.success(f"### Resultados para: {nombre}")
    res1, res2 = st.columns(2)
    res1.metric("VAN", f"{van:,.2f} €")
    res2.metric("Payback", payback_resultado)
    
    if van > 0:
        st.balloons()
        st.write("✅ **Conclusión:** El proyecto es viable.")
    else:
        st.write("❌ **Conclusión:** El proyecto no es rentable.")
