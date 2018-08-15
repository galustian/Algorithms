#define SHRESHOLD 0.01

double squareRoot(double y) {
    if (y == (double) 0) return 0;
    if (y < 0) {
        double d;
        *(int64_t*)&d = 0x7FF8000000000000;   // nan
        return -d;
    }
    
    // initial guess for x
    double x = 1;

    while (true) {
        // x1 = x - f(x) / f'(x)
        // f(x) = y - x^2
        // f'(x) = -2x
        double x1 = x + (y - x*x) / (2.0 * x);

        if ((x1 >= x && x1 - x < SHRESHOLD) || (x1 < x && x - x1 < SHRESHOLD)) {
            return x1;
        }
        x = x1;
    }
}