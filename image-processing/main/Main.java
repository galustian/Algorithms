package main;

import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;

import javax.imageio.ImageIO;

public class Main {
    public static void main(String[] args) throws IOException, Exception {
        BufferedImage img = ImageIO.read(new File("monalisa.png"));
        var gaussBlur = new GaussianBlur(5, 3);
        var gaussBlurredImg = gaussBlur.blurImage(img);

        try {
            ImageIO.write(gaussBlurredImg, "PNG", new File("monagauss.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        var meanBlur = new MeanBlur(5);
        var meanBlurredImg = meanBlur.blurImage(img);

        try {
            ImageIO.write(meanBlurredImg, "PNG", new File("monamean.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}