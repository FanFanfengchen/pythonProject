/*
 * 项目名称：Python项目演示页面
 * 描述：用于演示页面的交互功能脚本
 * 版本：1.0.0
 * 创建时间：2024
 */

function navigate(anId) {
  const problemDiv = document.getElementById("d" + anId);
  const previewDiv = document.getElementById("preview");

  if (previewDiv) {
    previewDiv.innerHTML = problemDiv !== null ? problemDiv.innerHTML : "Select a problem element in tree";
  }
}
