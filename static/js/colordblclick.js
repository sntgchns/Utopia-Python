const mail = document.querySelector('popup');
        const dot = document.querySelector('.dot');
        const sec = document.querySelector('.sec');
        const a = document.querySelector('a');
        dot.ondblclick = function(){
            dot.classList.toggle('active')
            sec.classList.toggle('active')
            a.classList.toggle('active')
            popup.classList.toggle('active')
        }
        document.addEventListener("mousemove", function(e){
            const dot = document.querySelector('.dot');
            dot.style.left = e.pageX + 'px';
            dot.style.top = e.pageY + 'px';
        })