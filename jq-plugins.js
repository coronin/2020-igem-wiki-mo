$(document).ready(function () {
  // 初始化加载class
  setTimeout(() => {
    $('[data-add]').addClass(function () {
      return $(this).attr('data-add')
    })
  }, 10)
  // 滚动条增加动画事件
  let idx = 0
  scrollAnimate()
  $(window).scroll(scrollAnimate)
  function scrollAnimate (e) {
    let _y = $(window).scrollTop()
    let _h = $(window).height()
    let item = $('[data-animated]')
    let len = item.length
    for (let i = idx; i < len; i ++) {
      item.eq(i).addClass('animated')
      let _iTop = item.eq(i).offset().top
      let _class = item.eq(i).attr('data-animated') + ' active-finished'
      
      if (_iTop - (_h + _y) < -50) {
        let _d = item.eq(i).attr('data-delay') || 0
        if (_d) {
          setTimeout(function () {
            item.eq(i).addClass(_class)
          }, parseFloat(_d))
        } else {
          item.eq(i).addClass(_class)
        }
        // idx = i
      }
    }
  }
})