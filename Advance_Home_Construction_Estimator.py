# ===== ADVANCE HOME CONSTRUCTION ESTIMATOR =====

BRICK_RATE = 8
CEMENT_BAG_RATE = 420
SAND_RATE = 1200
STEEL_RATE = 100
CONCRETE_RATE = 2000

PLASTER_RATE = 18
PUTTY_RATE = 12
PRIMER_RATE = 10
PAINT_RATE = 25

FLOORING_RATE = 80
TILE_RATE = 180

DOOR_RATE = 6000
WINDOW_RATE = 3000
VENTILATOR_RATE = 1500

WOOD_RATE = 1300
WOOD_LABOUR_RATE = 90

SWITCH_POINT_RATE = 350
FAN_POINT_RATE = 1200
LIGHT_POINT_RATE = 800
SOCKET_POINT_RATE = 500

WATER_POINT_RATE = 500
DRAIN_POINT_RATE = 400

WIRE_RATE_PER_M = 25
PIPE_RATE_PER_M = 80

BOUNDARY_WALL_RATE = 1500
GATE_RATE = 25000

LABOUR_RATE = 250

BRICK_L = 0.19
BRICK_W = 0.09
BRICK_H = 0.09


def estimator():

    print("\n===== ADVANCE HOME CONSTRUCTION ESTIMATOR =====")
     
    import streamlit as st

    plot_l = float(st.number_input("Plot length (m): "))
    plot_w = float(st.number_input("Plot width (m): "))

    floors = int(st.number_input("Number of floors: "))
    rooms = int(st.number_input("Number of rooms: "))
    bathrooms = int(st.number_input("Number of bathrooms: "))

    staircase_area = float(st.number_input("Staircase area (sq m): "))
    balcony_area = float(st.number_input("Balcony area (sq m): "))

    wall_h = float(st.number_input("Wall height (m): "))
    wall_t = float(st.number_input("Wall thickness (m): "))

    slab_t = float(st.number_input("Slab thickness (m): "))

    steel_dia = float(st.number_input("Steel diameter (mm): "))
    steel_len = float(st.number_input("Steel length (m): "))

    doors = int(st.number_input("Number of doors: "))
    windows = int(st.number_input("Number of windows: "))
    ventilators = int(st.number_input("Number of ventilators: "))

    wood_area = float(st.number_input("Woodwork area (sq ft): "))

    switch_points = int(st.number_input("Switch points: "))
    fan_points = int(st.number_input("Fan points: "))
    light_points = int(st.number_input("Light points: "))
    socket_points = int(st.number_input("Socket points: "))

    water_points = int(st.number_input("Water points: "))
    drain_points = int(st.number_input("Drain points: "))

    wire_length = float(st.number_input("Wire length (m): "))
    pipe_length = float(st.number_input("Water pipeline length (m): "))

    boundary_length = float(st.number_input("Boundary wall length (m): "))
    gates = int(st.number_input("Number of gates: "))

    floor_area_m2 = plot_l * plot_w

    builtup_m2 = (
        floor_area_m2 * floors
        + staircase_area
        + balcony_area
    )

    wall_volume = builtup_m2 * wall_h * wall_t

    brick_volume = BRICK_L * BRICK_W * BRICK_H

    bricks = (wall_volume / brick_volume) * 1.10

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

    # ===== COST GROUPS =====

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

    cost_per_sqft = total_cost / (builtup_m2 * 10.764)

    # ===== PROJECT SUMMARY =====

    st.subheader("\n========== PROJECT SUMMARY ==========")

    st.write(f"Plot Area: {floor_area_m2:.2f} m²")
    st.write(f"Built-up Area: {builtup_m2:.2f} m²")

    st.write(f"Floors: {floors}")
    st.write(f"Rooms: {rooms}")
    st.write(f"Bathrooms: {bathrooms}")

    st.write(f"Staircase Area: {staircase_area:.2f} m²")
    st.write(f"Balcony Area: {balcony_area:.2f} m²")

    # ===== MATERIAL SUMMARY =====

    st.subheader("\n========== MATERIAL SUMMARY ==========")

    st.write(f"Bricks Required : {int(bricks)} Nos")
    st.write(f"Cement Required : {cement:.2f} Bags")
    st.write(f"Sand Required   : {sand:.2f} m³")
    st.write(f"Steel Required  : {steel_weight:.2f} kg")
    st.write(f"Concrete Volume : {slab_volume:.2f} m³")

    # ===== COST BREAKDOWN =====

    st.subheader("\n========== COST BREAKDOWN ==========")

    st.write(f"Structural Cost : ₹{structural_cost:.2f}")
    st.write(f"Masonry Cost    : ₹{masonry_cost:.2f}")
    st.write(f"Finishing Cost  : ₹{finishing_cost:.2f}")
    st.write(f"Electrical Cost : ₹{electrical_cost:.2f}")
    st.write(f"Plumbing Cost   : ₹{plumbing_cost:.2f}")
    st.write(f"Joinery Cost    : ₹{joinery_cost:.2f}")
    st.write(f"External Cost   : ₹{external_cost:.2f}")
    st.write(f"Labour Cost     : ₹{labour_cost:.2f}")

    # ===== DETAILS =====

    st.subheader("\n========== DETAILED ITEMS ==========")

    st.write(f"Doors           : {doors}")
    st.write(f"Windows         : {windows}")
    st.write(f"Ventilators     : {ventilators}")

    st.write(f"Switch Points   : {switch_points}")
    st.write(f"Fan Points      : {fan_points}")
    st.write(f"Light Points    : {light_points}")
    st.write(f"Socket Points   : {socket_points}")

    st.write(f"Water Points    : {water_points}")
    st.write(f"Drain Points    : {drain_points}")

    st.write(f"Wire Length     : {wire_length:.2f} m")
    st.write(f"Pipeline Length : {pipe_length:.2f} m")

    st.write(f"Boundary Wall   : {boundary_length:.2f} m")
    st.write(f"Gates           : {gates}")

    st.subheader("\n====================================")
    st.write(f"TOTAL COST      : ₹{total_cost:.2f}")
    st.write(f"COST PER SQ FT  : ₹{cost_per_sqft:.2f}")
    st.write("====================================")


estimator()