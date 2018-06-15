package main;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.util.Arrays;

public class GaussianBlur {
    private final int radius;
    private final double sigma;
    private final double[][] kernel;

    public GaussianBlur(int radius, double sigma) throws Exception {
        if (radius % 2 == 0) throw new Exception("radius must be an odd integer");
        this.radius = radius;
        this.sigma = sigma;
        kernel = new double[radius][radius];
        generateKernel();
    }

    private void generateKernel() {
        double sum = 0;
        for (int i = 0; i < kernel.length; i++) {
            for (int j = 0; j < kernel[i].length; j++) {
                kernel[i][j] = gaussianDensity(i - radius / 2, j - radius / 2, sigma);
                sum += kernel[i][j];
            }
        }
        for (int i = 0; i < kernel.length; i++) {
            for (int j = 0; j < kernel[i].length; j++) {
                kernel[i][j] /= sum;
            }
        }
    }

    public BufferedImage blurImage(BufferedImage img) {
        var blurredImg = new BufferedImage(img.getWidth(), img.getHeight(), BufferedImage.TYPE_INT_RGB);

        for (int i = 0; i < img.getWidth(); i++) {
            for (int j = 0; j < img.getHeight(); j++) {
                Color[] neighborPixels = getNeighborPixels(img, i, j);
                int convolvedPixel = convolve(neighborPixels, img, i, j);
                blurredImg.setRGB(i, j, convolvedPixel);
            }
        }
        return blurredImg;
    }

    // w and h are Image Middle-Points
    private int convolve(Color[] neighborPixels, BufferedImage img, int w, int h) {
        
        /*System.out.println("IMG Height: " + (img.getHeight()-1));
        System.out.println("Current Point w: " + w);
        System.out.println("Current Point h: " + h);*/
        
        // find how many 
        int neighborPixelsRange = 0;
        int pxMaxI = 0;
        while (pxMaxI < neighborPixels.length && neighborPixels[pxMaxI] != null) {
            pxMaxI++;
            neighborPixelsRange = pxMaxI;
        }
        var kernelPixels = getKernelPixels(neighborPixelsRange, img, w, h);

        // Make convolved Pixel
        int red = 0;
        int green = 0;
        int blue = 0;

        for (int i = 0; i < neighborPixelsRange; i++) {
            red += neighborPixels[i].getRed() * kernelPixels[i];
            green += neighborPixels[i].getGreen() * kernelPixels[i];
            blue += neighborPixels[i].getBlue() * kernelPixels[i];
        }

        var newColor = new Color(red, green, blue);
        return newColor.getRGB();
    }

    // w and h are Image Middle-Points!
    private double[] getKernelPixels(int neighborPixelsRange, BufferedImage img, int w, int h) {
        var kernelPixels = new double[neighborPixelsRange];
            
        int colStartPX = 0;
        int colEndPX = radius;
        int rowStartPX = 0;
        int rowEndPX = radius;
        
        int kernelHalfLen = (radius - 1) / 2;

        if (w <= kernelHalfLen-1) {
            // Left Edge Surpassing
            colStartPX = kernelHalfLen - w;
        } else if (w + kernelHalfLen > img.getWidth()-1) {
            // Right Edge Surpassing
            colEndPX -= w + kernelHalfLen - (img.getWidth()-1);
        }

        if (h <= kernelHalfLen-1) {
            // Top Edge Surpassing
            rowStartPX = kernelHalfLen - h;
        } else if (h + kernelHalfLen > img.getHeight()-1) {
            // Bottom Edge Surpassing
            rowEndPX -= h + kernelHalfLen - (img.getHeight()-1);
        }
        
        int rowRange = rowEndPX-rowStartPX;
        for (int i = colStartPX; i < colEndPX; i++) {
            int colI = i - colStartPX;
            for (int j = rowStartPX; j < rowEndPX; j++) {
                int rowI = j - rowStartPX;
                kernelPixels[colI * rowRange + rowI] = kernel[i][j];
            }
        }

        return kernelPixels;
    }

    // w and h are Image Middle-Points!
    private Color[] getNeighborPixels(BufferedImage img, int w, int h) {
        var neighborPixels = new Color[radius*radius];

            var colRange = radius;
        var rowRange = radius;

        int colStartPX = w - (int) (colRange - 1) / 2;
        int rowStartPX = h - (int) (rowRange - 1) / 2;

        int kernelHalfLen = (radius - 1) / 2;

        // If filter surpasses column edge of image
        if (w <= kernelHalfLen-1) {
            // radius - how much kernel surpasses left edge
            colRange = radius - (kernelHalfLen - w);
            colStartPX = 0;
        } else if (w + kernelHalfLen > img.getWidth()-1) {
            // radius - how much kernel surpasses right edge
            colRange = radius - ((w + kernelHalfLen) - (img.getWidth()-1));
            colStartPX = (img.getWidth()-1) - colRange;
        }

        // If filter surpasses row edge of image
        if (h <= kernelHalfLen-1) {
            // radius - how much kernel surpasses top edge
            rowRange = radius - (kernelHalfLen - h);
            rowStartPX = 0;
        } else if (h + kernelHalfLen > img.getHeight()-1) {
            // radius - how much kernel surpasses bottom edge
            rowRange = radius - ((h + kernelHalfLen) - (img.getHeight()-1));
            rowStartPX = (img.getHeight()-1) - rowRange;
        }

        for (int i = 0; i < colRange; i++) {
            for (int j = 0; j < rowRange; j++) {
                neighborPixels[i*rowRange + j] = new Color(img.getRGB(colStartPX + i, rowStartPX + j));
            }
        }

        return neighborPixels;
    }
    
    private double gaussianDensity(double x, double y, double sigma) {
        return (1 / (2 * Math.PI * Math.pow(sigma, 2))) 
        * Math.exp(-(Math.pow(x, 2) + Math.pow(y, 2)) / (2 * Math.pow(sigma, 2)));
    } 
}