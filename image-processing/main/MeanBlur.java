package main;

public class MeanBlur extends Filter {
    public MeanBlur(int radius) throws Exception {
        super(radius);
        generateKernel();
    }

    private void generateKernel() {
        double sum = 0;
        for (int i = 0; i < super.radius; i++) {
            for (int j = 0; j < super.radius; j++) {
                super.kernel[i][j] = 1 / (double)(super.radius*super.radius);
                sum += super.kernel[i][j];
            }
        }
    }
}