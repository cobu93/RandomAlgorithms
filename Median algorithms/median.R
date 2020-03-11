#!/usr/bin/env Rscript

library('optparse')


r_select <- function(array, position){
    splitter = sample(1:length(array), 1, replace=TRUE)

    positive_part <- c()
    negative_part <- c()

    index <- 1

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

    d_pos <- floor(0.5 * (n ** 0.75) - sqrt(n))
    d_pos <- if(d_pos < 1) 1 else d_pos
    u_pos <- ceiling(0.5 * (n ** 0.75) + sqrt(n))

    d <- r_subset[d_pos]
    u <- r_subset[u_pos]

    C <- c()
    l_d <- 0
    l_u <- 0

    for(element in array){
        if((element >= d) & (element <= u)){
            C <- c(C, element)
        }

        if(element < d){
            l_d <- l_d + 1
        }
        else if(element > u){
            l_u <- l_u + 1
        }
    }

    if((l_d > n / 2) | (l_u > n / 2)){
        return(c(NULL, 1.0))
    }

    if(length(C) > 4 * (n ** 0.75)){
        return(c(None, 1.0))
    }

    return(c(sort(C)[floor(n / 2) - l_d], n ** -0.25))
}

option_list = list(
    make_option(c('--length', '-l'), type='integer', default=NA, help='Array length.'),
    make_option(c('--max', '-m'), type='integer', default=NA, help='Max value in array.'),
    make_option(c('--reps', '-r'), type='integer', default=5, help='Repetitions for r_median algorithm.')
); 
 
parser = OptionParser(option_list=option_list);
args = parse_args(parser);

if (is.na(args$length) | is.na(args$max)) {
    stop('length and max must be provided')
}

random_array <- sample(1:args$max, args$length, replace=TRUE)

rs_start_time = Sys.time()
r_select_median <- r_select(random_array, ceiling(length(random_array) / 2))
rs_end_time = Sys.time()

rm_start_time = Sys.time()
r_m_median <- NULL
r_median_prob <- 1.0
for(i in 1:args$reps){
    r_median_results <- r_median(random_array)
    i_r_median <- r_median_results[1]
    i_r_median_prob <- r_median_results[2]
    if(!is.null(i_r_median)){
        r_median_prob <- r_median_prob * i_r_median_prob
        if(is.null(r_m_median)){
            r_m_median <- i_r_median
        }
        else if(r_m_median != i_r_median){
            stop('Medians were distinct!') 
        }
    }
}
rm_end_time = Sys.time()

lower_median <- floor((length(random_array) - 1) / 2) + 1
real_medians <- sort(random_array)[lower_median]

cat('Real median:', real_medians, '\n', sep=' ')
cat('R-Select median:', r_select_median, '\tElapsed time:', (rs_end_time - rs_start_time), 'seconds\n', sep=' ')
cat('R-Median median:', r_m_median, '\tProbability:', 1 - r_median_prob, '\tElapsed time:', (rm_end_time - rm_start_time), 'seconds\n', sep=' ')