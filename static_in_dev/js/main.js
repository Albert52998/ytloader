// let div1 = document.getElementById('div1');
// let div2 = document.getElementById('div2');
// let div3 = document.getElementById('div3');
// let div4 = document.getElementById('div4');
// let div5 = document.getElementById('div5');
// function ShowHide() {
// 	// setTimeout(function() {
// 	// 	div1.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
// 	// 	div2.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
// 	// 	div3.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
// 	// 	div4.style.background = 'linear-gradient(to top,#ff8a00,#da1b60)';
// 	// 	div5.style.background = 'linear-gradient(to top,#ff8a00,#da1b60)';	
// 	// }, 1000);
// }
// ShowHide();


const bannerBtn = document.getElementById('banner__btn');
const loadingText = document.getElementById('loading-text');
//const vDownload = document.getElementById('v-download');

bannerBtn.addEventListener('click', function() {
	if(loadingText.style.display = 'none') {
		loadingText.style.display = 'block';
	}
	else if(loadingText.style.display = 'block') {
		loadingText.style.display = 'none'
	}
});
//
//if(loadingText.style.display = 'none') {
//	vDownload.style.display = 'inline-block';
//}
	
