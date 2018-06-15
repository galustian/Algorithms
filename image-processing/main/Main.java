package main;

import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;

import javax.imageio.ImageIO;

public class Main {
    public static void main(String[] args) throws IOException, Exception {
        BufferedImage img = ImageIO.read(new File("monalisa.png"));
        var gaussBlur = new GaussianBlur(5, 3);
        var blurredImg = gaussBlur.blurImage(img);

        try {
            ImageIO.write(blurredImg, "PNG", new File("monagauss.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}