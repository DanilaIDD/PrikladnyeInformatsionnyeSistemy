var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        console.log("you clicked ", event.target);
        var post = event.target.parentElement.parentElement;
        var articleInfo = post.querySelector('.article-info');
        var articleText = post.querySelector('.article-text');
        if (post.classList.contains('folded')) {
            event.target.innerHTML = "Свернуть";
            post.classList.remove('folded');
            articleInfo.style.display = 'block';
            articleText.style.display = 'block';
        } else {
            event.target.innerHTML = "Развернуть";
            post.classList.add('folded');
            articleInfo.style.display = 'none';
            articleText.style.display = 'none';
        }
    });
}