/*
 * 项目名称：Python项目演示页面
 * 描述：用于演示页面的交互功能脚本
 * 版本：1.0.0
 * 创建时间：2024
 */

const DEFAULT_NAVIGATE_CONFIG = {
  idPrefix: "d",
  previewElementId: "preview",
  defaultMessage: "Select a problem element in tree"
};

function navigate(anId, config = {}) {
  if (!anId || typeof anId !== 'string') {
    console.warn('Invalid anId provided to navigate function');
    return;
  }

  const mergedConfig = { ...DEFAULT_NAVIGATE_CONFIG, ...config };
  const { idPrefix, previewElementId, defaultMessage } = mergedConfig;

  if (!idPrefix || !previewElementId || typeof defaultMessage !== 'string') {
    console.error('Invalid configuration: idPrefix, previewElementId and defaultMessage are required');
    return;
  }

  const problemDiv = document.getElementById(`${idPrefix}${anId}`);
  const previewDiv = document.getElementById(previewElementId);

  if (previewDiv) {
    previewDiv.innerHTML = problemDiv !== null ? problemDiv.innerHTML : defaultMessage;
  } else {
    console.warn(`Preview element with ID "${previewElementId}" not found`);
  }
}
