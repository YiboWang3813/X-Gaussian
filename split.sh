
# remove simple-knn 
git submodule deinit -f submodules/simple-knn 
git rm -f submodules/simple-knn 
rm -rf .git/modules/submodules/simple-knn 

# clone simple-knn as the normal way 
git clone https://github.com/camenduru/simple-knn.git simple-knn
rm -rf simple-knn/.git
git add simple-knn 
git commit -m "add simple-knn as a normal dir"

# remove SIBR_viewers 
git submodule deinit -f SIBR_viewers
git rm -f SIBR_viewers
rm -rf .git/modules/SIBR_viewers
