from sys import argv
from PIL import Image

def generate_gif(duration):
    blue = Image.open("./high_quality_gif_files/background/blue_rectangle.png")
    blue_rgba = blue.convert("RGBA")
    helmet_and_words = Image.open("./high_quality_gif_files/background/helmet_and_words.png")
    helmet_and_words_rgba = helmet_and_words.convert("RGBA")
    blue_rgba.paste(helmet_and_words_rgba, (0, 0), helmet_and_words_rgba)
    bg = blue_rgba.copy()

    frames = []
    for i in range(45):
        frames.append(bg.copy())
        ith_degree = Image.open(f"./high_quality_gif_files/gear/{i:02d}_degree.png")
        ith_degree_rgba = ith_degree.convert("RGBA")
        frames[i].paste(ith_degree_rgba, (0, 0), ith_degree_rgba)

    filename = "gear.gif"

    frames[0].save(f"./high_quality_gif_files/{filename}", save_all=True, append_images=frames[1:], duration=duration, disposal=2, loop=0)
    print(f"Generated {filename} at ./high_quality_gif_files/{filename}")

if __name__ == "__main__":
    if len(argv) == 2:
        generate_gif(int(argv[1]))
    else:
        print("Usage: python generate_gif.py <duration>")