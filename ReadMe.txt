				userNumber1=parseInt(prompt("Enter the number obtiained for Number 1: "));
				userNumber2=parseInt(prompt("Enter the number obtiained for Number 2: "));
				userNumber3=parseInt(prompt("Enter the number obtiained for Number 3: "));
				userNumber4=parseInt(prompt("Enter the number obtiained for Number 4: "));
				userNumber5=parseInt(prompt("Enter the number obtiained for Number 5: "));
				userNumber6=parseInt(prompt("Enter the number obtiained for Number 6: "));
				
				
				document.getElementById("draw").innerHTML = <span>+"lotteryNum1"+</span><span>+"lotteryNum2"+</span><span>+"lotteryNum3"+</span><span>+"lotteryNum4"+</span><span>+"lotteryNum5"+</span><span>+"lotteryNum6"+</span><span>+"lotteryNum7"</span>;


                if((userNumber1==lotteryNum1)||(userNumber1==lotteryNum2)||(userNumber1==lotteryNum3)||(userNumber1==lotteryNum4)||(userNumber1==lotteryNum5)||(userNumber1==lotteryNum6)||(userNumber1==lotteryNum7)){
					document.getElementById("displayUserNum1").classList.add("highlightWin");
				}
                if((userNumber2==lotteryNum1)||(userNumber2==lotteryNum2)||(userNumber2==lotteryNum3)||(userNumber2==lotteryNum4)||(userNumber2==lotteryNum5)||(userNumber2==lotteryNum6)||(userNumber2==lotteryNum7)){
					document.getElementById("displayUserNum2").classList.add("highlightWin");
				}
                if((userNumber3==lotteryNum1)||(userNumber3==lotteryNum2)||(userNumber3==lotteryNum3)||(userNumber3==lotteryNum4)||(userNumber3==lotteryNum5)||(userNumber3==lotteryNum6)||(userNumber3==lotteryNum7)){
					document.getElementById("displayUserNum3").classList.add("highlightWin");
				}
                if((userNumber4==lotteryNum1)||(userNumber4==lotteryNum2)||(userNumber4==lotteryNum3)||(userNumber4==lotteryNum4)||(userNumber4==lotteryNum5)||(userNumber4==lotteryNum6)||(userNumber4==lotteryNum7)){
					document.getElementById("displayUserNum4").classList.add("highlightWin");
				}
                if((userNumber5==lotteryNum1)||(userNumber5==lotteryNum2)||(userNumber5==lotteryNum3)||(userNumber5==lotteryNum4)||(userNumber5==lotteryNum5)||(userNumber5==lotteryNum6)||(userNumber5==lotteryNum7)){
					document.getElementById("displayUserNum5").classList.add("highlightWin");
				}
                if((userNumber6==lotteryNum1)||(userNumber6==lotteryNum2)||(userNumber6==lotteryNum3)||(userNumber6==lotteryNum4)||(userNumber6==lotteryNum5)||(userNumber6==lotteryNum6)||(userNumber6==lotteryNum7)){
					document.getElementById("displayUserNum6").classList.add("highlightWin");
				}
			