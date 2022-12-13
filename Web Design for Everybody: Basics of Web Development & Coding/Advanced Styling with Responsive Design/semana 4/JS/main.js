function upDate(previewPic){

originalClass=document.getElementById('image').style.backgroundImage;
originalText=document.getElementById('image').innerHTML;

document.getElementById('image').style.backgroundImage= 'url(' + previewPic.src + ')';
document.getElementById('image').innerHTML = previewPic.alt;
console.log(previewPic);
//previewPic.style.display="inline";
	}

	function unDo(){
    
document.getElementById('image').style.backgroundImage = originalClass;
document.getElementById('image').innerHTML = originalText;
//previewPic.style.display="none";
	}
