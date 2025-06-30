<!-- 🔷 الصفحة الرئيسية index.html -->
... (المحتوى السابق للصفحات العامة يبقى كما هو) ...

<!-- 🔷 لوحة التحكم dashboard.html -->
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>لوحة التحكم</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</head>
<body>
  <!-- 🔹 شريط العنوان -->
  <div class="dashboard-header">
    <h1>لوحة التحكم - الإدارة</h1>
    <button onclick="toggleTheme()">تبديل المظهر</button>
    <a href="/logout" class="logout-btn">تسجيل الخروج</a>
  </div>

  <!-- 🔹 قسم الفلاتر -->
  <form method="GET" class="filter-form">
    <input type="text" name="name" placeholder="اسم الطالب">
    <input type="text" name="department" placeholder="الاختصاص">
    <input type="text" name="year" placeholder="السنة الدراسية">
    <input type="text" name="subject" placeholder="المادة">
    <input type="date" name="date" placeholder="التاريخ">
    <button type="submit">فلترة</button>
  </form>

  <!-- 🔹 جدول عرض الطلاب -->
  <table class="data-table">
    <thead>
      <tr>
        <th>الاسم</th>
        <th>اسم الأب</th>
        <th>ID</th>
        <th>الاختصاص</th>
        <th>السنة</th>
        <th>نسبة الحضور</th>
        <th>خيارات</th>
      </tr>
    </thead>
    <tbody>
      {% for student in students %}
      <tr>
        <td>{{ student[1] }}</td>
        <td>{{ student[2] }}</td>
        <td>{{ student[3] }}</td>
        <td>{{ student[4] }}</td>
        <td>{{ student[5] }}</td>
        <td>{{ student[7] or '0%' }}</td>
        <td>
          <a href="/edit/{{ student[0] }}">تعديل</a> |
          <a href="/export/{{ student[0] }}">تصدير</a>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>

  <!-- 🔹 زر التصدير الكامل -->
  <div class="export-controls">
    <a href="/export_all" class="export-btn">تصدير كل البيانات</a>
  </div>

</body>
</html>
