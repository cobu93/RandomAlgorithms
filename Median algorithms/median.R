
r_select <- function(array, position){
    splitter = sample(1:length(array), 1, replace=TRUE)

    positive_part <- c()
    negative_part <- c()

    index <- 0

    for(element in array){
        
        if(element <= array[splitter] && index != splitter){
            negative_part <- c(negative_part, element)
        }
        else if(element > array[splitter]){
            positive_part <- c(positive_part, element)
        }
        index <- index + 1
    }


    if(length(negative_part) == position - 1){
        return(array[splitter])
    }
    else if(length(negative_part) >= position){
        return(r_select(negative_part, position))
    }
    else{
        return(r_select(positive_part, position - 1 - length(negative_part)))
    }
}

r_median <- function(array){
    n <- length(array)
    r_subset <- sample(array, ceiling(n ** 0.75))
    r_subset <- sort(r_subset)

    d_pos <- floor(0.5 * (n ** 0.75) - sqrt(n)) - 1
    d_pos = if(d_pos < 0) 0 else d_pos
    u_pos = ceiling(0.5 * (n ** 0.75) + sqrt(n)) - 1

    d <- r_subset[d_pos]
    u <- r_subset[u_pos]

    C <- c()
    l_d <- 0
    l_u <- 0

    for(element in array){
        if(element >= d && element <= u){
            C <- c(C, element)
        }

        if(element < d){
            l_d <- l_d + 1
        }
        else if(element > u){
            l_u <- l_u + 1
        }
    }

    if(l_d > n / 2 || l_u > n / 2){
        return(None, 1.0)
    }

    if(length(C) > 4 * (n ** 0.75)){
        return(None, 1.0)
    }

    return(sort(C)[floor(n / 2) - l_d], n ** -0.25) 
}


#parser = argparse.ArgumentParser(description='Get median of random array of integers.')
#parser.add_argument('length', type=int, help='Array length.')
#parser.add_argument('max', type=int, help='Max value in array.')
#parser.add_argument('-r', '--reps', required=False, type=int, default=5, help='Repetitions for r_median algorithm.')
#
#args = parser.parse_args()
#
#
#random_array = np.random.randint(1, args.max + 1, size=args.length)
#
#rs_start_time = time.time()
#r_select_median = r_select(random_array.tolist(), math.ceil(len(random_array) / 2))
#rs_end_time = time.time()
#
#
#rm_start_time = time.time()
#r_m_median = None
#r_median_prob = 1.0
#for i in range(0, args.reps):
#    i_r_median, i_r_median_prob = r_median(random_array)
#    if i_r_median is not None:
#        r_median_prob *= i_r_median_prob
#        if r_m_median is None:
#            r_m_median = i_r_median
#        elif r_m_median != i_r_median:
#            raise Exception('Medians were distinct! ({}, {})'.format(r_m_median, i_r_median)) 
#
#rm_end_time = time.time()
#
#
#lower_median = math.floor((random_array.shape[0] - 1)/ 2)
#upper_median = math.ceil((random_array.shape[0] - 1) / 2)
#real_medians = np.sort(random_array)[[lower_median, upper_median]]
#
#print('Real medians:{}'.format(real_medians))
#print('R-Select median:{}    Elapsed time:{} seconds'.format(r_select_median, rs_end_time - rs_start_time))
#print('R-Median median:{}    Probability:{}    Elapsed time:{} seconds'.format(r_m_median, 1 - r_median_prob, rm_end_time - rm_start_time))


random_array <- sample(1:100, 10, replace=TRUE)


lower_median <- floor((length(random_array) - 1) / 2) + 1
upper_median <- ceiling((length(random_array) - 1) / 2) + 1
real_medians <- sort(random_array)[c(lower_median, upper_median)]

r_select_median <- r_select(random_array, ceiling(length(random_array) / 2))
print(sort(random_array))
print(real_medians)
print(r_select_median)