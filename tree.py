import math

h_tree = 720 # height of tree (excluding base)
w_tree = 600 # widht of tree (at widest point)
h_layer = 12 # height of one layer
h_section = 3*h_layer # height of one section (2 branches + 2 stem sections)
num_sections = int(h_tree // h_section)


# Step 1: Compute (half) upper angle
lower_angle = math.atan(h_tree / (w_tree/2))
upper_angle = math.radians(90) - lower_angle
print(f"upper angle: {math.degrees(upper_angle)}")
print(f"lower angle: {math.degrees(lower_angle)}")

def w_branch(h):
    return 2 * h * math.tan(upper_angle)


total_area = 3 * 200*200 + 3*20*20
for i in range(0,num_sections):
    w = w_branch(h_tree - i * h_section)
    total_area += 2 * (w * 20) + 20*20
    print(f"with in {i}th section: {w} mm")

print(f"total_area: {total_area / (100**3)} m^2")
