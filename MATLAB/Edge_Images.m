%% 
% Read in image and create the non noisy images needed for What is an Edge?
img = imread('Edge_Example.png');
imGray = rgb2gray(img);

figure;
imshow(imGray);

[m,n] = size(imGray);
scanLine = int32(imGray(90,:));

% figure;
% imshow(scanLine);

imRed = img;
imRed(90,:,1) = 255;
imRed(90,:,2) = 0;
imRed(90,:,3) = 0;

% Original image with scan line
figure;
imshow(imRed);
title('Edge Image')

% Intensity Image
figure;
p1 = plot(scanLine);
axis([0 200 -50 300]);
p1.Color = 'black';
p1.LineWidth = 2;
title('Intensity Plot');
xlabel('Horizontal Pixel');
ylabel('Pixel Intensity');

% Derivative
dy = diff(scanLine);
figure;
p2 = plot(dy);
axis([0 200 -150 150]);
p2.Color = 'black';
p2.LineWidth = 2;
title('Derivative of Intensity Plot');
xlabel('Horizontal Pixel');
ylabel('Pixel Gradient');

%% Add noise and create the same images over

imN = imnoise(img,'gaussian');
imNoise = imnoise(imN,'gaussian');
imNoise = imnoise(imNoise,'gaussian');
imNoise = imnoise(imNoise,'gaussian');
imNoise = imnoise(imNoise,'gaussian');
imNoise = imnoise(imNoise,'gaussian');
imGray2 = rgb2gray(imNoise);

figure;
imshow(imGray2);

[m,n] = size(imGray2);
scanLine2 = int32(imGray2(90,:));

imRed2 = imNoise;
imRed2(90,:,1) = 255;
imRed2(90,:,2) = 0;
imRed2(90,:,3) = 0;

% Original image with scan line
figure;
imshow(imRed2);
title('Edge Image with Noise')

% Intensity Image
figure;
p1 = plot(scanLine2);
axis([0 200 -50 300]);
p1.Color = 'black';
p1.LineWidth = 2;
title('Intensity Plot of Noisy Edge');
xlabel('Horizontal Pixel');
ylabel('Pixel Intensity');

% Derivative
dy = diff(scanLine2);
figure;
p2 = plot(dy);
axis([0 200 -150 150]);
p2.Color = 'black';
p2.LineWidth = 2;
title('Derivative of Noisy Intensity Plot');
xlabel('Horizontal Pixel');
ylabel('Pixel Gradient');
