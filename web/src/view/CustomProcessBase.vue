<template>
  <div class="custom-tree-container">
    <!-- <div class="block">
    <p>使用 render-content</p>
    <el-tree
      :data="data"
      show-checkbox
      node-key="id"
      default-expand-all
      :expand-on-click-node="false"
      :render-content="renderContent">
    </el-tree>
  </div> -->
    <div class="block">    
    <!-- <div style="text-align: center">      
      <el-button
        type="success"
        icon="el-icon-plus"
        @click="() => rootAppend()"
      >
      </el-button>     
    </div> -->
    <el-tree
      :data="data"
      show-checkbox
      node-key="id"
      default-expand-all
      :expand-on-click-node="false">
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <span>{{ node.label }}</span>
        <span>
          <el-button type="text" @click="editLabel(node, data)">编辑</el-button>
          <el-button
            type="text"
            size="mini"
            @click="() => append(data)">
            添加
          </el-button>
          <el-button
            type="text"
            size="mini"
            @click="() => remove(node, data)">
            删除
          </el-button>
        </span>
      </span>
    </el-tree>
  </div>
    <div style="text-align:center">
      <el-button type="success" icon="el-icon-check" circle @click="submitData"></el-button>
      <el-button type="danger" icon="el-icon-delete" circle @click="deleteAll"></el-button>
    </div>
  <!-- <div>
    <el-row>
      <el-button icon="el-icon-search" circle></el-button>
      <el-button type="primary" icon="el-icon-edit" circle></el-button>
      <el-button type="info" icon="el-icon-message" circle></el-button>
      <el-button type="warning" icon="el-icon-star-off" circle></el-button>
    </el-row>
  </div> -->
  </div>
</template>
<script>
import axios from "axios";
// import qs from 'qs'
let id = 1000;

export default {
  data() {
    // id：唯一标识
    // parent_id：父级的唯一标识
    //     1、他自身的抽象、模板
    //     2、父级
    // condition，条件
    //     other_obj.fields：
    //     fields：
    // desc：描述
    // result，结果
    //     key：value

    // 时间：创建时间，更新时间

    // 人：SysUser   rel表
    // 机：Machine   rel表
    // 物：Good   rel表
    // 环：Environment   rel表
    const data = [
      {
        id: 0,        
        label: "id",
        children: [
        ],
      },
      {
        id: 1,        
        label: "condition",
        children: [
        ],
      },
      {
        id: 2,        
        label: "desc",
        children: [
        ],
      },
      {
        id: 3,        
        label: "result",
        children: [
        ],
      },
    ];
    return {
      data: JSON.parse(JSON.stringify(data)),
      // data: JSON.parse(JSON.stringify(data))
    };
  },

  methods: {
    jiaohuanneirong() {
      console.log("jiaohuanneirong this.data");
    },
    submitData() {
      console.log("submitData this.data");
      console.log(this.data);
      // axios.post("http://127.0.0.1:5000/new", qs.stringify(this.data))

      //在需要的事件中直接使用
      axios({
        url: "http://127.0.0.1:5000/new",
        method: "post",
        data: this.data,
        header: {
          "Content-Type": "application/json", //如果写成contentType会报错
        },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((Error) => {
          console.log(Error);
        });
    },
    deleteAll() {
      console.log("deleteAll this.data");
      console.log(this.data);
    },
    append(data) {
      this.$prompt("请输入新的名称", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          console.log(value);
          
          const idNew = id + 1;
          id++;
          const newChild = { id: idNew, label: value, children: [] };
          if (!data.children) {
            this.$set(data, "children", []);
          }
          data.children.push(newChild);

          this.$message({
            type: "success",
            message: "成功: " + value,
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },

    remove(node, data) {
      console.log(node);
      console.log(data);
      const parent = node.parent;
      const children = parent.data.children || parent.data;
      const index = children.findIndex((d) => d.id === data.id);
      children.splice(index, 1);
    },

    renderContent(h, { node, data, store }) {
      console.log(store);
      return (
        <span class="custom-tree-node">
          <span>{node.label}</span>
          <span>
            <el-button
              size="mini"
              type="text"
              on-click={() => this.append(data)}
            >
              Append
            </el-button>
            <el-button
              size="mini"
              type="text"
              on-click={() => this.remove(node, data)}
            >
              Delete
            </el-button>
          </span>
        </span>
      );
    },

    editLabel(node, data) {
      console.log(node);
      console.log(data);

      this.$prompt("请输入新的名称", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          console.log(value);
          this.$set(data, "label", value);
          this.$message({
            type: "success",
            message: "成功: " + value,
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },    
    rootAppend() {
      this.$prompt("请输入新的名称", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          console.log(value);
          console.log(this.data);
          
          const idNew = id + 1;
          id++;
          const newChild = { id: idNew, label: value, children: [] };
          
          this.data.push(newChild);

          console.log(this.data);

          this.$message({
            type: "success",
            message: "成功: " + value,
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },
  },
};
</script>


<style>
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
.custom-tree-container {
  display: inline-grid;
}
</style>
