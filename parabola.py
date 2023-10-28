def quadratic_parabola_graph_thing_with_the_turning_point_method(turning_point_x, turning_point_y, y_intercept):
    turning_point_x_inverted = (0 - turning_point_x)
    a = (y_intercept - turning_point_y) / ((turning_point_x_inverted ** 2) if turning_point_x_inverted != 0 else 1)
    return "y = " + str(a if a != 0 else 1) + "(x+" + str(turning_point_x_inverted) + ")^2 " + " +" + str(turning_point_y) if not (turning_point_y == 0) else ""


# this will run on casio calculators (that's why we didnt use f"")
turning_point_x = int(input("whar is da x value?"))
turning_point_y = int(input("whar is da y value?"))
y_intercept = int(input("whar is da y intercept?"))
print(quadratic_parabola_graph_thing_with_the_turning_point_method(turning_point_x, turning_point_y, y_intercept))
