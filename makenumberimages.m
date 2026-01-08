for i =0:2393

    arr = ones([256,256]);
    arr = uint16(arr*i);
    index = arrayfun(@(x) sprintf('%04u', x), arr(1), 'UniformOutput', false);
    

    imwrite(arr, strcat('G:\pdgfb2_imagenumber\pdgfb2_pos',string(index(1)),'.png'))
end

%%

img = imread('G:\pdgfb3_restitch_imagenumber\pdgfb3_posimg_tumorarea.tif');

imgusenumpdgfb3 = unique(img)

%%
stroutput = [];
for k = 1:length(imgusenumpdgfb3)
    num = sprintf('%04u',imgusenumpdgfb3(k));
    strrow = strcat('pdgfb3_pos_',string(num));
    stroutput = [stroutput;strrow];
end

writematrix(stroutput,'G:\pdgfb3_restitch_imagenumber\pdgfb3_tumorarea.txt')