git
rm - r - -cached.venv
git
add.
git
commit - m
"Fix project structure"
git
push


def evaluate_polynomial(poly_dict, x):
    res = 0

    for i in poly_dict:
        coef = poly_dict[i]
        res += coef * (x**i)
    return res

my_poly = {
    0: -10,
    2: 3,
    4: 1
}
#check x^2-2x+25
#if x=1 -> 1^2-2*1+25=1-2+25=24
#if x=2 -> 2^2-2*2+25=4-4+25=25
my_poly_2 = {
    0: 25,
    1: -2,
    2: 1
}

result_1 = evaluate_polynomial(my_poly, 2)
result_2 = evaluate_polynomial(my_poly, -1.5)

#Check
result_3 = evaluate_polynomial(my_poly_2, 1)
result_4 = evaluate_polynomial(my_poly_2, 2)

print("P(2) =", result_1)
print("P(-1.5) =", result_2)


print("-"*16)
print("check P(1) =", result_3)
print("check P(2) =", result_4)
print("-"*16)