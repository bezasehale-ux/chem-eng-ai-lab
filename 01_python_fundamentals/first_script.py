# Chemical Engineering Python Start 
print("Hello I am Chemical Engineering Student!")
print("This is my first Python script for chemical engineering") 
print("Let's begin the journey!")

# Chemical Engineering Calculations
print("\n=== Chemical Engineering Calculations ===")

# Reactor conversion
initial_conc = input('Initial Concentration (mol/L): ')  # mol/L
conversion = input('Conversion rate (%): ')  # % as input

# Convert percentage to decimal
conversion_decimal = float(conversion) / 100
final_conc = float(initial_conc) * (1 - conversion_decimal)

print(f"Reactor - Final concentration: {final_conc} mol/L")

# Mass Balance
print("\n--- Mass Balance ---")
feed_rate = input('Feed rate (kg/hr): ')  # kg/hr
yield_percent = input('Yield (%): ')  # % as input

# Convert percentage to decimal
yield_decimal = float(yield_percent) / 100
product_rate = float(feed_rate) * yield_decimal

print(f"Mass Balance - Product rate: {product_rate} kg/hr")

# Energy Calculation
print("\n--- Energy Calculation ---")
mass = input('Mass of material (kg): ')  # kg
specific_heat = input('Specific heat capacity (kJ/kg°C): ')  # kJ/kg°C
temp_change = input('Temperature change (°C): ')  # °C

energy = float(mass) * float(specific_heat) * float(temp_change)

print(f"Energy Required: {energy} kJ")

print("\n🎉 AI CHEMICAL ENGINEERING JOURNEY BEGINS!")