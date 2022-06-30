## Flex



#### 1. 배치의 흐름

```html
<body>
	<div class="flex-container">
    <div class="flex-item">AAAAAAAAAAAA</div>
    <div class="flex-item">BBBBB</div>
    <div class="flex-item">CCCCCCCCCCC</div>
  </div>
</body>
```

: Flex 아이템들은 가로 방향으로 배치되며, 자신이 가진 내용의 width만큼 차지한다.height는 컨테이너의 높이 만큼 늘어나게 된다. 

```html
  <style>
    .flex-container{
      display:flex;
    }
  </style>
```

![image-20220620092800112](Flex.assets/image-20220620092800112.png)



inline-flex는 컨테이너가 자신이 가진 내용물에 width 가 맞춰진다. 

```html
  <style>
    .flex-container{
      display:inline-flex;
    }
  </style>
```

![image-20220620092822305](Flex.assets/image-20220620092822305.png)



##### :heavy_check_mark:(1) flex-direction

```html
<body>
	<div class="flex-container">
    <div class="flex-item">1111111111</div>
    <div class="flex-item">22222</div>
    <div class="flex-item">333333</div>
  </div>
</body>
```

- row (default)

  ```css
    <style>
      .flex-container{
        display:flex;
      }
    </style>
  ```

  ![image-20220620093423450](Flex.assets/image-20220620093423450.png)

- row-reverse

  ```html
    <style>
      .flex-container{
        display:flex;
        flex-direction: row-reverse;
      }
    </style>
  ```

  ![image-20220620093503196](Flex.assets/image-20220620093503196.png)

- column

  ```html
    <style>
      .flex-container{
        display:flex;
        flex-direction: column;
      }
    </style>
  ```

  ![image-20220620093545129](Flex.assets/image-20220620093545129.png)

- column-reverse

  ```html
    <style>
      .flex-container{
        display:flex;
        flex-direction: column-reverse;
      }
    </style>
  ```

  ![image-20220620093616736](Flex.assets/image-20220620093616736.png)



##### :heavy_check_mark: (2) flex-wrap

: 컨테이너가 아이템들을 한 줄에 담을 여유 공간이 없을 때, 줄바꿈을 통해 아이템을 어떻게 배치할 지 결정하는 속성이다.

기본값은 nowrap 으로 줄바꿈 없이 밖으로 빠져나가도 내용을 한 줄에 들고 있으려고 한다. 

![image-20220620094128616](Flex.assets/image-20220620094128616.png)



- wrap

  ```html
    <style>
      .flex-container{
        display:flex;
        flex-wrap: wrap;
      } 
    </style>
  ```

  ![image-20220620094226732](Flex.assets/image-20220620094226732.png)



- wrap-reverse

  ```html
    <style>
      .flex-container{
        display:flex;
        flex-wrap: wrap-reverse;
      } 
    </style>
  ```

  ![image-20220620094311823](Flex.assets/image-20220620094311823.png)



##### :heavy_check_mark: (3) flex-flow

: flex-direction과 flex-wrap을 한 번에 지정할 수 있는 단축 속성이다.

flex-direction, flex-wrap의 순으로 한 칸 떼고 쓰면 된다.

```
  <style>
    .flex-container{
      display:flex;
      felx-flow: row-reverse wrap;
    } 
  </style>
```

 











----------



#### 2. 아이템 정렬

##### :heavy_check_mark:(1) justify-content 

: 메인 축(row, column, row-reverse...) 위에서 정렬.

```html
	<style>
		.flex-container {
			display: flex;
			justify-content: flex-start;
			/* justify-content: flex-end; */
			/* justify-content: center; */
			/* justify-content: space-between; */
			/* justify-content: space-around; */
			/* justify-content: space-evenly; */
		}
	</style>
```

- flex-start

  

  ![image-20220620104128630](Flex.assets/image-20220620104128630.png)

- flex-end

  

  ![image-20220620104153582](Flex.assets/image-20220620104153582.png)

- center

  : 양 끝의 공백 크기 같고, 가운데로 정렬하기.

  

  ![image-20220620104638929](Flex.assets/image-20220620104638929.png)

- space-between

  

  ![image-20220620104744309](Flex.assets/image-20220620104744309.png)

- space-around

  

  ![image-20220620104907168](Flex.assets/image-20220620104907168.png)

- space-evenly

  

  ![image-20220620105004176](Flex.assets/image-20220620105004176.png)





##### :heavy_check_mark:(2) align-items

```html
	<style>
		.flex-container {
			display: flex;
			align-items: stretch;
			/* align-items: flex-start; */
			/* align-items: flex-end; */
			/* align-items: center; */
			/* align-items: baseline; */
			height: 300px;
		}
	</style>
```

```html
<body>
	<div class="flex-container">
		<div class="flex-item">AAAAAAAAAAAA</div>
		<h1 class="flex-item">BBBBBBBB</h1>
		<div class="flex-item">CCCCCCC</div>
	</div>
</body>
```



- stretch

  : container 의 height에 맞추어 item이 늘어나 정렬된다.

  ![image-20220620131150233](Flex.assets/image-20220620131150233.png)

  

- flex-start

  : container 의 윗 부분을 기준으로 정렬된다. 

  ![image-20220620131306728](Flex.assets/image-20220620131306728.png)

​		

- flex-end

  :container 의 아랫 부분을 기준으로 정렬된다.

  ![image-20220620131419891](Flex.assets/image-20220620131419891.png)

  

  

- flex-center

  : container의 가운데로 item이 정렬된다.

  ![image-20220620131517204](Flex.assets/image-20220620131517204.png)

- baseline

  : 텍스트의 베이스라인을 기준으로 정렬한다.

  ![image-20220620131607153](Flex.assets/image-20220620131607153.png)





- container의 정 가운데로 아이템을 정렬하기 위해서는 justify-content, align-items를 center 설정하면 된다. 

```
	<style>
		.flex-container {
			display: flex;
			justify-content:center;
			align-items: center;
			height: 300px;
		}
	</style>
```





##### :heavy_check_mark: (3) align-content

: flex-wrap : wrap; 이 설정되어있는 상태에서, 아이템들의 행이 2줄 이상일 때 수직축 방향 정렬하는 속성



- stratch (default)
- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly











---------



#### 3. Flex 아이템에 적용가능한 속성들



##### (1) flex-basis

: Flex item의 기본 크기를 설정한다. flex-direction이 row일 때에는 너비, column일 때에는 높이 값을 나타낸다. 

width로 설정하면 원래 100px이 넘는 item도 100px로 맞추어지지만, flex-basis의 경우 100px이 안되는 item만 100px으로 늘어나고 100px이 넘는 item은 원래의 크기를 유지한다. 



##### (2) flex-grow

: flex-grow에 들어가는 숫자의 의미는 flex-basis를 제외한 여백의 부분을 flex-grow에 지정된 숫자의 비율로 나누어가진다는 뜻이다. 

```html
	<style>
		.flex-container {
			display: flex;
		}
		.flex-item {
			flex-grow: 1;
		}
		.flex-item:nth-child(2) {
			flex-grow: 4;
		}
	</style>
```

![image-20220620135136347](Flex.assets/image-20220620135136347.png)



##### (3) flex-shrink

: flex-shrink 를 0으로 세팅하면 아이템의 크기가 flex-basis보다 작아지지 않는다. 이를 통해 고정되어있는 크기의 컬럼을 만들 수 있다. 



#### (4) flex  --> 축약 속성!

: flex-grow, flex-shrink, flex-basis 순서

```
.item{
	flex: 1;
}
```

- flex-grow: 1, flex-shrink:1, flex-basis:0% 를 의미한다.



```
.item{
	flex: 1 1 auto;
}
```

- flex-grow: 1, flex-shrink:1, flex-basis:auto 를 의미한다.



```
.item{
	flex: 1 500px;
}
```

- flex-grow: 1, flex-shrink:1, flex-basis:500px를 의미한다.







---------



