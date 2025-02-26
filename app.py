import streamlit as st
from datetime import datetime
import math

# Set page config
st.set_page_config(
    page_title="Professional Unit Converter",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for professional styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f8f9fa;
        padding: 0;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(90deg, #1a237e, #283593);
        padding: 2rem 3rem;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .app-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: white;
    }
    
    .app-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        border-left: 4px solid #3f51b5;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }
    
    /* Result styling */
    .result-container {
        background: linear-gradient(135deg, #3f51b5, #5c6bc0);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(63, 81, 181, 0.2);
        margin: 2rem 0;
    }
    
    .result-value {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .result-equals {
        font-size: 1.5rem;
        opacity: 0.8;
        margin: 0.5rem 0;
    }
    
    /* Form controls styling */
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
    }
    
    .stNumberInput > div > div > input {
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
        padding: 0.5rem 1rem !important;
    }
    
    /* Section headers */
    .section-header {
        color: #3f51b5;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
    }
    
    /* Common conversions styling */
    .common-conversion {
        background-color: #f5f7ff;
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #c5cae9;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        color: #666;
        font-size: 0.9rem;
        border-top: 1px solid #e0e0e0;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-163ttbj {
        background-color: #f1f3f9 !important;
    }
    
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1a237e;
        margin-bottom: 1rem;
    }
    
    /* Category badges */
    .category-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        background-color: #e8eaf6;
        color: #3f51b5;
    }
    
    /* Formula styling */
    .formula-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .header-container {
            padding: 1.5rem;
        }
        
        .app-title {
            font-size: 2rem;
        }
        
        .result-value {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="app-title">Professional Unit Converter</h1>
    <p class="app-subtitle">Convert between different units of measurement with precision and ease</p>
</div>
""", unsafe_allow_html=True)

# Define conversion categories and their units with icons
conversion_categories = {
    "📏 Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "⚖️ Weight/Mass": ["kilogram", "gram", "milligram", "metric_ton", "pound", "ounce"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "🧪 Volume": ["liter", "milliliter", "cubic_meter", "gallon", "quart", "pint", "cup", "fluid_ounce"],
    "📐 Area": ["square_meter", "square_kilometer", "hectare", "acre", "square_foot", "square_inch"],
    "⏱️ Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "🔌 Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour", "electron_volt"],
    "💻 Digital": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
}

# Create sidebar for category selection
st.sidebar.markdown('<div class="sidebar-header">Conversion Settings</div>', unsafe_allow_html=True)

# Display all categories as badges
st.sidebar.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
for cat in conversion_categories.keys():
    st.sidebar.markdown(f'<span class="category-badge">{cat}</span>', unsafe_allow_html=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Category selection
category = st.sidebar.selectbox("Select Conversion Category", list(conversion_categories.keys()))

# Get units for the selected category
units = conversion_categories[category]
category_clean = category.split(" ")[1]  # Remove emoji

# Add information about the category
category_info = {
    "Length": "Length is a measure of distance. Units range from microscopic to astronomical scales.",
    "Weight/Mass": "Weight is the force exerted on an object due to gravity, while mass is the amount of matter in an object.",
    "Temperature": "Temperature is a measure of heat energy in a system. Different scales have different reference points.",
    "Volume": "Volume measures the three-dimensional space occupied by a substance or object.",
    "Area": "Area measures the extent of a two-dimensional surface or region.",
    "Time": "Time measures the duration between events or the intervals during which events occur.",
    "Energy": "Energy is the capacity to do work or produce heat. It exists in various forms like kinetic, potential, thermal, etc.",
    "Digital": "Digital units measure data storage capacity and transfer rates in computing systems."
}

st.sidebar.markdown(f"""
<div class="card" style="margin-top: 1rem;">
    <h4 style="margin-top: 0;">{category_clean} Units</h4>
    <p>{category_info.get(category_clean, "")}</p>
</div>
""", unsafe_allow_html=True)

# Add last updated info
current_time = datetime.now().strftime("%B %d, %Y")
st.sidebar.markdown(f"""
<div class="footer" style="margin-top: 2rem; padding: 1rem; font-size: 0.8rem;">
    <p>Last Updated: {current_time}</p>
    <p>Version 2.0</p>
</div>
""", unsafe_allow_html=True)

# Main content
container = st.container()

with container:
    # Create a card for the conversion form
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Create two columns for input and output
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<h3 style="color: #3f51b5; margin-top: 0;">From</h3>', unsafe_allow_html=True)
        from_unit = st.selectbox("Convert from", units, key="from_unit")
        value = st.number_input("Enter value", value=1.0, step=0.01, format="%.6f")

    with col2:
        st.markdown('<h3 style="color: #3f51b5; margin-top: 0;">To</h3>', unsafe_allow_html=True)
        to_unit = st.selectbox("Convert to", units, key="to_unit")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Conversion functions for each category
    def convert_length(value, from_unit, to_unit):
        # Conversion to meters (base unit)
        length_to_meter = {
            "meter": 1,
            "kilometer": 1000,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "mile": 1609.34,
            "yard": 0.9144,
            "foot": 0.3048,
            "inch": 0.0254
        }
        
        # Convert from source unit to meters, then to target unit
        meters = value * length_to_meter[from_unit]
        return meters / length_to_meter[to_unit]
    
    def convert_weight(value, from_unit, to_unit):
        # Conversion to kilograms (base unit)
        weight_to_kg = {
            "kilogram": 1,
            "gram": 0.001,
            "milligram": 0.000001,
            "metric_ton": 1000,
            "pound": 0.453592,
            "ounce": 0.0283495
        }
        
        # Convert from source unit to kg, then to target unit
        kg = value * weight_to_kg[from_unit]
        return kg / weight_to_kg[to_unit]
    
    def convert_temperature(value, from_unit, to_unit):
        # Special handling for temperature
        if from_unit == to_unit:
            return value
        
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "celsius" and to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5/9
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            return value - 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    def convert_volume(value, from_unit, to_unit):
        # Conversion to liters (base unit)
        volume_to_liter = {
            "liter": 1,
            "milliliter": 0.001,
            "cubic_meter": 1000,
            "gallon": 3.78541,
            "quart": 0.946353,
            "pint": 0.473176,
            "cup": 0.236588,
            "fluid_ounce": 0.0295735
        }
        
        # Convert from source unit to liters, then to target unit
        liters = value * volume_to_liter[from_unit]
        return liters / volume_to_liter[to_unit]
    
    def convert_area(value, from_unit, to_unit):
        # Conversion to square meters (base unit)
        area_to_sq_meter = {
            "square_meter": 1,
            "square_kilometer": 1000000,
            "hectare": 10000,
            "acre": 4046.86,
            "square_foot": 0.092903,
            "square_inch": 0.00064516
        }
        
        # Convert from source unit to square meters, then to target unit
        sq_meters = value * area_to_sq_meter[from_unit]
        return sq_meters / area_to_sq_meter[to_unit]
    
    def convert_time(value, from_unit, to_unit):
        # Conversion to seconds (base unit)
        time_to_second = {
            "second": 1,
            "minute": 60,
            "hour": 3600,
            "day": 86400,
            "week": 604800,
            "month": 2629746,  # Average month (30.44 days)
            "year": 31556952   # Average year (365.24 days)
        }
        
        # Convert from source unit to seconds, then to target unit
        seconds = value * time_to_second[from_unit]
        return seconds / time_to_second[to_unit]
    
    def convert_energy(value, from_unit, to_unit):
        # Conversion to joules (base unit)
        energy_to_joule = {
            "joule": 1,
            "kilojoule": 1000,
            "calorie": 4.184,
            "kilocalorie": 4184,
            "watt_hour": 3600,
            "kilowatt_hour": 3600000,
            "electron_volt": 1.602176634e-19
        }
        
        # Convert from source unit to joules, then to target unit
        joules = value * energy_to_joule[from_unit]
        return joules / energy_to_joule[to_unit]
    
    def convert_digital(value, from_unit, to_unit):
        # Conversion to bits (base unit)
        digital_to_bit = {
            "bit": 1,
            "byte": 8,
            "kilobyte": 8 * 1024,
            "megabyte": 8 * 1024**2,
            "gigabyte": 8 * 1024**3,
            "terabyte": 8 * 1024**4
        }
        
        # Convert from source unit to bits, then to target unit
        bits = value * digital_to_bit[from_unit]
        return bits / digital_to_bit[to_unit]

    # Perform the conversion based on the selected category
    try:
        if category_clean == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif category_clean == "Weight/Mass":
            result = convert_weight(value, from_unit, to_unit)
        elif category_clean == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category_clean == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        elif category_clean == "Area":
            result = convert_area(value, from_unit, to_unit)
        elif category_clean == "Time":
            result = convert_time(value, from_unit, to_unit)
        elif category_clean == "Energy":
            result = convert_energy(value, from_unit, to_unit)
        elif category_clean == "Digital":
            result = convert_digital(value, from_unit, to_unit)
        else:
            result = None
            st.error("Conversion category not supported.")
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")
        result = None

    # Display the result
    if result is not None:
        st.markdown(f"""
        <div class="result-container">
            <p style="margin-bottom: 0; opacity: 0.8;">Conversion Result</p>
            <div class="result-value">
                {value:.6g} {from_unit}
            </div>
            <div class="result-equals">
                = {result:.6g} {to_unit}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Create a two-column layout for formula and common conversions
    col1, col2 = st.columns(2)
    
    with col1:
        # Add a formula explanation in a card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">Conversion Formula</h3>', unsafe_allow_html=True)
        
        st.markdown('<div class="formula-container">', unsafe_allow_html=True)
        if category_clean == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                st.latex(r"F = C \times \frac{9}{5} + 32")
            elif from_unit == "celsius" and to_unit == "kelvin":
                st.latex(r"K = C + 273.15")
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                st.latex(r"C = (F - 32) \times \frac{5}{9}")
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                st.latex(r"K = (F - 32) \times \frac{5}{9} + 273.15")
            elif from_unit == "kelvin" and to_unit == "celsius":
                st.latex(r"C = K - 273.15")
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                st.latex(r"F = (K - 273.15) \times \frac{9}{5} + 32")
            else:
                st.latex(f"{from_unit} = {to_unit}")
        else:
            st.markdown(f"Standard unit conversion using conversion factors between {from_unit} and {to_unit}.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Add common conversion examples in a card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">Common Conversions</h3>', unsafe_allow_html=True)
        
        if category_clean == "Length":
            st.markdown('<div class="common-conversion">1 meter = 3.28084 feet</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 kilometer = 0.621371 miles</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 inch = 2.54 centimeters</div>', unsafe_allow_html=True)
        elif category_clean == "Weight/Mass":
            st.markdown('<div class="common-conversion">1 kilogram = 2.20462 pounds</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 pound = 16 ounces</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 metric ton = 1000 kilograms</div>', unsafe_allow_html=True)
        elif category_clean == "Temperature":
            st.markdown('<div class="common-conversion">0°C = 32°F = 273.15K (Freezing point of water)</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">100°C = 212°F = 373.15K (Boiling point of water)</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">20°C = 68°F = 293.15K (Room temperature)</div>', unsafe_allow_html=True)
        elif category_clean == "Volume":
            st.markdown('<div class="common-conversion">1 liter = 0.264172 gallons</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 gallon = 3.78541 liters</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 cup = 8 fluid ounces</div>', unsafe_allow_html=True)
        elif category_clean == "Area":
            st.markdown('<div class="common-conversion">1 square meter = 10.7639 square feet</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 acre = 4046.86 square meters</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 hectare = 10,000 square meters</div>', unsafe_allow_html=True)
        elif category_clean == "Time":
            st.markdown('<div class="common-conversion">1 day = 24 hours = 1440 minutes = 86400 seconds</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 year ≈ 365.25 days (accounting for leap years)</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 month ≈ 30.44 days (average)</div>', unsafe_allow_html=True)
        elif category_clean == "Energy":
            st.markdown('<div class="common-conversion">1 kilowatt-hour = 3.6 megajoules</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 calorie = 4.184 joules</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 kilocalorie = 1000 calories (food calorie)</div>', unsafe_allow_html=True)
        elif category_clean == "Digital":
            st.markdown('<div class="common-conversion">1 byte = 8 bits</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 kilobyte = 1024 bytes</div>', unsafe_allow_html=True)
            st.markdown('<div class="common-conversion">1 gigabyte = 1024 megabytes</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Add a tips section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-header">Pro Tips</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <ul>
        <li><strong>Precision matters:</strong> For scientific calculations, consider using more decimal places.</li>
        <li><strong>Unit systems:</strong> Be aware of which system (metric, imperial) you're working with.</li>
        <li><strong>Significant figures:</strong> Maintain appropriate significant figures for your application.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2023 Professional Unit Converter | Created with Streamlit</p>
    <p>Built with precision and reliability</p>
</div>
""", unsafe_allow_html=True)