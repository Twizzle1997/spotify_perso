from skimage import io
import matplotlib.pyplot as plt

class Recommendation():

    def visualize_cover(self, playlist_df):
        temp = playlist_df['album_img'].values
        plt.figure(figsize=(15,int(0.625 * len(temp))) , facecolor='#8F7C7C')
        columns = 5
        
        for i, url in enumerate(temp):
            plt.subplot(int(len(temp) / columns + 1), int(columns), int(i + 1))

            image = io.imread(url)
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])
            s=' ' 
            plt.xlabel(s.join(playlist_df['name'].values[i].split(' ')[:4]), fontsize = 11, fontweight='bold')
            plt.tight_layout(h_pad=0.8, w_pad=0)
            plt.subplots_adjust(wspace=None, hspace=None)

        plt.show()