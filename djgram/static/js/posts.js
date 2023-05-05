likeClick = (btnId) =>{
    const like_btn = document.getElementById(btnId);
    console.log(like_btn)
    const like_icon = like_btn.querySelector("i");
    like_icon.classList.replace("fa-regular", "fa-solid");
}