use bmp::Pixel;
use bmp::Image;
const IMAGE_SIZE_PX : u32 = 256;

fn main() {
    let mut img = Image::new(IMAGE_SIZE_PX, IMAGE_SIZE_PX);

    for x in 0..IMAGE_SIZE_PX {
        for y in 0..IMAGE_SIZE_PX {
            let xf = (x as f32 - IMAGE_SIZE_PX as f32 / 2.0) / (IMAGE_SIZE_PX as f32 / 2.0);
            let yf = -(y as f32 - IMAGE_SIZE_PX as f32 / 2.0) / (IMAGE_SIZE_PX as f32 / 2.0);

            if (xf.powi(2) + yf.powi(2) - 0.3).powi(3) - xf.powi(2) * yf.powi(3) < 0.0 {
                img.set_pixel(x, y, Pixel::new(255, 0, 0));
            } else {
                img.set_pixel(x, y, Pixel::new(255, 255, 255));
            }
        }
    }

    img.save("heart.bmp").expect("Error: Cannot save image!");
}
