<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div>
	<div>
		<label for="">用户名：</label><input type="text" v-model="username"><br>
		<label for="">密码：</label><input type="text" v-model="password"><br>
		<button @click="requestToken">发起请求Token</button>
	</div>
	<div>
		<label for="">创建分类：</label><input type="text" v-model="categoryName"><br>
		<button @click="requestCreateCategory">创建</button>
	</div>
	<div>
		<label for="">id：</label><input type="text" v-model="categoryId"><br>
		<label for="">修改分类：</label><input type="text" v-model="newCategoryName"><br>
		<button @click="requestUpdateCategory">修改</button>
	</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	return{
		username:"wjw",
		password:"w0330j0329w",
		categoryName:"",
		categoryId:"",
		newCategoryName:""
	}  
  },
  components: {
    // HelloWorld
  },
  methods:{
	  requestCategoryList(){
		  // console.log("点击了")
		  // 获取分类列表
		  this.$api.getCategoryList().then(res=>{
			  console.log("得到列表",res);
		  }).catch(err=>{
			  console.log("发生错误",err);
		  })

	  },
	  requestToken(){
		  this.$api.getToken({
			  username:this.username,
			  password:this.password
		  }).then(res=>{
		  		console.log("得到Token",res);
				this.$jsCookie.set("refresh",res.data.refresh);
				this.$jsCookie.set("access",res.data.access);
		  }).catch(err=>{
		  		console.log("发生错误",err);
		  })
		  
	  },
	  requestCreateCategory(){
		  if (this.categoryName != ""){
			  this.$api.createCategory({
			  		name:this.categoryName
			  }).then(res=>{
			  		console.log("新建分类",res);
			  }).catch(err=>{
			  		console.log("发生错误",err);
			  })
		  }
		  else{
			  console.log("不能为空");
		  }
	  },
	  requestUpdateCategory(){
		  if(this.categoryId != ""){
			  if(this.newCategoryName != ""){
				  this.$api.updateCategory({
					  id:this.categoryId,
					  name:this.newCategoryName
				  }).then(res=>{
			  		console.log("修改后的数据",res);
				  }).catch(err=>{
			  		console.log("发生错误",err);
			  })
			  }else{
				  console.log("分类名不能为空");
			  }
		  }else{
			  console.log("id不能为空");
		  }
	  }
  }
}
</script>
