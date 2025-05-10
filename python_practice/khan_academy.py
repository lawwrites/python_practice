def calc_b(r, sx, sy):
    b = r * (sy/sx)
    return b

def calc_a(r, sx, sy, y, x):
    slope = calc_b(r, sx, sy)
    a = y - (slope * x )
    return round(a,2) 

def calc_lsl(r, sx, sy, y, x):
    constant = calc_a(r, sx, sy, y, x)
    slope = calc_b(r, sx, sy)
    lsl = constant + slope * x 
    y = round(lsl,2)
    print(f"Least Squares Regression Line is: y = {constant} + {slope}x\n Y: {y} ")

# run_it = calc_lsl(.81, 14.8, 177.6, 696, 75.8) 





# def run_calc():
#     calc_lst()

# Obtain the pop size
# obtain the sample survey size
# calculate the response variable for the sample size
# multiple the result to the pop size for estimate

def population(pop_size):
    pop = pop_size
    return pop

def sample(samp,response):
    samp_size = sum(samp)
    response_percentage = response/samp_size
    return response_percentage

def estimate(pop_size, samp, response):
    get_pop = population(pop_size)
    get_response_percentage = sample(samp, response)
    get_estimate =  get_pop * get_response_percentage
    print(f"Population: {get_pop}\n Estimate (Based Off Sample): {get_estimate}")

# store_pop = population(414)
# print(store_pop)

# store_samp = sample([15,9,10,8,3], 10)
# print(store_samp)

# store_estimate = estimate(414,[15,9,10,8,3], 10)
# print(store_estimate)

#standard deviation
#subtract each datapoint from the mean
#sum the results
#divide by n-1
#take the square root

def vr(dp, the_mean):
    lst = []

    for x in dp:
        result = x - the_mean
        lst.append(result)
    print(f"the dps are: {lst}")
    sum_result = sum(lst)
    print(f"The sum of dps are: {sum_result}")
    len_lst = len(lst)
    samp_corr = len_lst - 1
    return sum_result/samp_corr

get_variance = vr([2,2,2,2,2,2,2,2,2,2,2,2],2)
print(get_variance)

