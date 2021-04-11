# BigNumber


BigNumber is an arbitrary precision number library which 
supports numbers with any values and many operations with them.

# Installation

pip install BigNumber

# Usage

To use this library, install it using the command shown in 
"Installation" section. Then, read the instructions below 
regarding how to use operations with BigNumber.

## Addition

BigNumber can be added with any numbers using "+" operator.

## Subtraction

BigNumber can be subtracted by any numbers using "-" operator.

## Multiplication

BigNumber can be multiplied with any numbers using "*" operator.

## Division

BigNumber can be divided by any numbers using "+" operator.

## Modulo

The "%" sign can be used together with BigNumber for modulo
operations.

## Integer Division

The "//" sign can be used together with BigNumber for modulo
operations.

## Exponents

BigNumber can be raised to the power of any other numbers using "**" operator.

## Conversion to int

int(BigNumber("5.3"))  # 5

## Conversion to float

float(BigNumber("5.3"))  # 5.0

## Conversion to mpf

to_mpf(BigNumber("5.0))  # 5.0

## Trigonometric Functions

**sin**, **cos**, **tan**, **cosec**, **sec**, and **cot** are 
usable trigonometric functions. They are called using the code 
with the format **{trigonometric function name}(a big number object)**.
For example, sin(BigNumber("0.5")) to get the value of sin(0.5).

## Hyperbolic Functions

**sinh**, **cosh**, **tanh**, **cosech**, **sech**, and **coth** are 
usable hyperbolic functions. They are called using the code 
with the format **{hyperbolic function name}(a big number object)**.
For example, sinh(BigNumber("0.5")) to get the value of sinh(0.5).

## Factorial

The function **factorial(big_num: BigNumber)** will quickly get the 
factorial of any number.

## Logarithms

The logarithm of any number using any base can be quickly achieved by 
using the function **log_base(big_num: BigNumber, base: BigNumber or mpf or float or int)**
where big_num is a **BigNumber** object and **base** is the base used for 
the logarithm operation.

## Square Root

**sqrt(big_num: BigNumber)** gets the square root of any number.

## Cube Root

**cbrt(big_num: BigNumber)** gets the cube root of any number.

## Square

**BigNumber.squared()** gets the value of a BigNumber squared.

## Cube

**BigNumber.cubed()** gets the value of a BigNumber cubed.

# Running Tests

The script "BigNumber_versus_mpf.py" 
(https://github.com/GlobalCreativeCommunityFounder/BigNumber/blob/main/BigNumber/BigNumber_versus_mpf.py)
is used to run tests of the performance of BigNumber
library against mpf library.

# Sample Test Results

An example of test results for BigNumber versus mpf is in the 
file "BigNumber_versus_mpf.txt"
(https://github.com/GlobalCreativeCommunityFounder/BigNumber/blob/main/BigNumber/BigNumber_versus_mpf.txt).
