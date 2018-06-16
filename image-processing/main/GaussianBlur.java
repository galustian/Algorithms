package main;

public class GaussianBlur extends Filter {
    private final double sigma;

    public GaussianBlur(int radius, double sigma) throws Exception {
        super(radius);
        this.sigma = sigma;
        generateKernel();
    }

    private void generateKernel() {
        double sum = 0;
        for (int i = 0; i < super.radius; i++) {
            for (int j = 0; j < super.radius; j++) {
                super.kernel[i][j] = gaussianDensity(i - super.radius / 2, j - super.radius / 2, sigma);
                sum += super.kernel[i][j];
            }
        }
        for (int i = 0; i < super.radius; i++) {
            for (int j = 0; j < super.radius; j++) {
                super.kernel[i][j] /= sum;
            }
        }
    }
    
    private double gaussianDensity(double x, double y, double sigma) {
        return (1 / (2 * Math.PI * Math.pow(sigma, 2))) 
        * Math.exp(-(Math.pow(x, 2) + Math.pow(y, 2)) / (2 * Math.pow(sigma, 2)));
    } 
}