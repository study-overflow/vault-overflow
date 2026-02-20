---
title: CSS变量入门
date: 2024-03-15
tags: [前端, CSS]
description: CSS变量的基本使用方法介绍
publish: true
---

# CSS变量入门

CSS 变量（也称为 CSS 自定义属性）是一种强大的功能，允许您在 CSS 中定义可重用的值。

## 定义变量

```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
}
```

## 使用变量

```css
.header {
  color: var(--primary-color);
  background-color: var(--secondary-color);
}
```

这样就可以在整个样式表中重复使用这些颜色值，提高了代码的可维护性。