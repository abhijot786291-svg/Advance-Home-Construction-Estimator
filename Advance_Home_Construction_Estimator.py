import streamlit as st

st.set_page_config(page_title="Advance Home Construction Estimator",
                   page_icon="🏠",
                   layout="wide")

st.title("🏠 Advance Home Construction Estimator")

# ===== RATES =====

BRICK_RATE = 12
CEMENT_BAG_RATE = 390
SAND_RATE = 1800
STEEL_RATE = 68
CONCRETE_RATE = 5500

PLASTER_RATE = 35
PUTTY_RATE = 18
PRIMER_RATE = 15
PAINT_RATE = 40

FLOORING_RATE = 180
TILE_RATE = 300

DOOR_RATE = 12000
WINDOW_RATE = 6000
VENTILATOR_RATE = 2500

WOOD_RATE = 2200
WOOD_LABOUR_RATE = 150

SWITCH_POINT_RATE = 600
FAN_POINT_RATE = 1800
LIGHT_POINT_RATE = 1200
SOCKET_POINT_RATE = 800

WATER_POINT_RATE = 900
DRAIN_POINT_RATE = 700

WIRE_RATE_PER_M = 45
PIPE_RATE_PER_M = 140

BOUNDARY_WALL_RATE = 2500
GATE_RATE = 50000

LABOUR_RATE = 550

BRICK_L = 0.19
BRICK_W = 0.09
BRICK_H = 0.09
plot_l = st.number_input("Plot length (m)", min_value=0.0)
plot_w = st.number_input("Plot width (m)", min_value=0.0)

floors = st.number_input("Number of floors", min_value=0, step=1)
rooms = st.number_input("Number of rooms", min_value=0, step=1)
bathrooms = st.number_input("Number of bathrooms", min_value=0, step=1)

staircase_area = st.number_input("Staircase area (sq m)", min_value=0.0)
balcony_area = st.number_input("Balcony area (sq m)", min_value=0.0)

wall_h = st.number_input("Wall height (m)", min_value=0.0)
wall_t = st.number_input("Wall thickness (m)", min_value=0.0)

slab_t = st.number_input("Slab thickness (m)", min_value=0.0)

steel_dia = st.number_input("Steel diameter (mm)", min_value=0.0)
steel_len = st.number_input("Steel length (m)", min_value=0.0)

doors = st.number_input("Number of doors", min_value=0, step=1)
windows = st.number_input("Number of windows", min_value=0, step=1)
ventilators = st.number_input("Number of ventilators", min_value=0, step=1)

wood_area = st.number_input("Woodwork area (sq ft)", min_value=0.0)

switch_points = st.number_input("Switch points", min_value=0, step=1)
fan_points = st.number_input("Fan points", min_value=0, step=1)
light_points = st.number_input("Light points", min_value=0, step=1)
socket_points = st.number_input("Socket points", min_value=0, step=1)

water_points = st.number_input("Water points", min_value=0, step=1)
drain_points = st.number_input("Drain points", min_value=0, step=1)

wire_length = st.number_input("Wire length (m)", min_value=0.0)
pipe_length = st.number_input("Pipeline length (m)", min_value=0.0)

boundary_length = st.number_input("Boundary wall length (m)", min_value=0.0)
gates = st.number_input("Number of gates", min_value=0, step=1)
construction_quality = st.selectbox(
    "Construction Quality",
    ["Basic", "Standard", "Premium"]
)

if construction_quality == "Basic":
    LABOUR_RATE = 450
    PAINT_RATE = 30
    TILE_RATE = 200
    DOOR_RATE = 8000
    FLOORING_RATE = 120

elif construction_quality == "Standard":
    LABOUR_RATE = 550
    PAINT_RATE = 40
    TILE_RATE = 300
    DOOR_RATE = 12000
    FLOORING_RATE = 180

else:  # Premium
    LABOUR_RATE = 700
    PAINT_RATE = 60
    TILE_RATE = 500
    DOOR_RATE = 20000
    FLOORING_RATE = 350
# ===== CALCULATIONS =====

floor_area_m2 = plot_l * plot_w

builtup_m2 = (
    floor_area_m2 * floors
    + staircase_area
    + balcony_area
)

wall_volume = builtup_m2 * wall_h * wall_t

brick_volume = BRICK_L * BRICK_W * BRICK_H

bricks = (wall_volume / brick_volume) * 1.10 if brick_volume > 0 else 0

mortar = wall_volume * 0.30

sand = mortar * 0.70

cement = mortar * 6.5

slab_volume = builtup_m2 * slab_t

steel_weight = (steel_dia ** 2 / 162) * steel_len

plaster_area = builtup_m2 * (
    3.5 + rooms * 0.2 + bathrooms * 0.3
)

paint_area = plaster_area
putty_area = plaster_area
primer_area = paint_area

flooring_area = builtup_m2

bathroom_tile_area = bathrooms * 20

# ===== COST CALCULATIONS =====

brick_cost = bricks * BRICK_RATE
cement_cost = cement * CEMENT_BAG_RATE
sand_cost = sand * SAND_RATE

steel_cost = steel_weight * STEEL_RATE
slab_cost = slab_volume * CONCRETE_RATE

plaster_cost = plaster_area * PLASTER_RATE
putty_cost = putty_area * PUTTY_RATE
primer_cost = primer_area * PRIMER_RATE
paint_cost = paint_area * PAINT_RATE

flooring_cost = flooring_area * FLOORING_RATE
tile_cost = bathroom_tile_area * TILE_RATE

door_cost = doors * DOOR_RATE
window_cost = windows * WINDOW_RATE
ventilator_cost = ventilators * VENTILATOR_RATE

wood_cost = wood_area * WOOD_RATE
wood_labour = wood_area * WOOD_LABOUR_RATE

switch_cost = switch_points * SWITCH_POINT_RATE
fan_cost = fan_points * FAN_POINT_RATE
light_cost = light_points * LIGHT_POINT_RATE
socket_cost = socket_points * SOCKET_POINT_RATE

wire_cost = wire_length * WIRE_RATE_PER_M

water_cost = water_points * WATER_POINT_RATE
drain_cost = drain_points * DRAIN_POINT_RATE
pipe_cost = pipe_length * PIPE_RATE_PER_M

boundary_cost = boundary_length * BOUNDARY_WALL_RATE
gate_cost = gates * GATE_RATE

labour_cost = builtup_m2 * LABOUR_RATE

structural_cost = steel_cost + slab_cost

masonry_cost = (
    brick_cost +
    cement_cost +
    sand_cost
)

finishing_cost = (
    plaster_cost +
    putty_cost +
    primer_cost +
    paint_cost +
    flooring_cost +
    tile_cost
)

electrical_cost = (
    switch_cost +
    fan_cost +
    light_cost +
    socket_cost +
    wire_cost
)

plumbing_cost = (
    water_cost +
    drain_cost +
    pipe_cost
)

joinery_cost = (
    door_cost +
    window_cost +
    ventilator_cost +
    wood_cost +
    wood_labour
)

external_cost = (
    boundary_cost +
    gate_cost
)

total_cost = (
    structural_cost +
    masonry_cost +
    finishing_cost +
    electrical_cost +
    plumbing_cost +
    joinery_cost +
    external_cost +
    labour_cost
)

# ===== BUTTON =====

if st.button("Calculate Estimate"):

    if builtup_m2 <= 0:
        st.error("Please enter valid plot dimensions and floors.")

    else:
        cost_per_sqft = total_cost / (builtup_m2 * 10.7639)

        st.success(f"💰 Total Cost: ₹{total_cost:,.2f}")
        st.info(f"📏 Cost Per Sq Ft: ₹{cost_per_sqft:,.2f}")

        st.write(f"🏠 Construction Quality: {construction_quality}")
        
        st.subheader("📋 Project Summary")

        st.write(f"Plot Area: {floor_area_m2:.2f} m²")
        st.write(f"Built-up Area: {builtup_m2:.2f} m²")
        st.write(f"Floors: {floors}")
        st.write(f"Rooms: {rooms}")
        st.write(f"Bathrooms: {bathrooms}")

        st.subheader("🧱 Material Summary")

        st.write(f"Bricks Required: {int(bricks)} Nos")
        st.write(f"Cement Required: {cement:.2f} Bags")
        st.write(f"Sand Required: {sand:.2f} m³")
        st.write(f"Steel Required: {steel_weight:.2f} kg")
        st.write(f"Concrete Volume: {slab_volume:.2f} m³")

        st.subheader("💵 Cost Breakdown")

        st.write(f"Structural Cost: ₹{structural_cost:,.2f}")
        st.write(f"Masonry Cost: ₹{masonry_cost:,.2f}")
        st.write(f"Finishing Cost: ₹{finishing_cost:,.2f}")
        st.write(f"Electrical Cost: ₹{electrical_cost:,.2f}")
        st.write(f"Plumbing Cost: ₹{plumbing_cost:,.2f}")
        st.write(f"Joinery Cost: ₹{joinery_cost:,.2f}")
        st.write(f"External Cost: ₹{external_cost:,.2f}")
        st.write(f"Labour Cost: ₹{labour_cost:,.2f}")
        