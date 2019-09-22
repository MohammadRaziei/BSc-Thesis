name = 'rzbinary_car-scheme.jpg';
image = im2double(imread(name));
image = heaviside(image-0.5);
imwrite(image,[name '.png'])
