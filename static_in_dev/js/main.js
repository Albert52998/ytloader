// let divCommon = document.getElementById('div-common');
let div1 = document.getElementById('div1');
let div2 = document.getElementById('div2');
let div3 = document.getElementById('div3');
let div4 = document.getElementById('div4');
let div5 = document.getElementById('div5');
function ShowHide() {
	setTimeout(function() {
		if(div1.style.background = '#ccc') {
			// alert('background gradient');
			div1.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
			div2.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
			div3.style.background = 'linear-gradient(to bottom,#ff8a00,#da1b60)';
			div4.style.background = 'linear-gradient(to top,#ff8a00,#da1b60)';
			div5.style.background = 'linear-gradient(to top,#ff8a00,#da1b60)';
			// ShowHide();
			setTimeout(function() {
				div1.style.background = '#ccc';
			}, 1000)
		}
		// else if(div1.style.background = 'linear-gradient(to top,#ff8a00,#da1b60);') {
		// 	// alert('background #ccc');
		// 	div1.style.background = '#ccc';
		// 	ShowHide();
		// }
		
	}, 1000);
}
ShowHide();
