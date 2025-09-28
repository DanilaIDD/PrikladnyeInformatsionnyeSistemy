var groupmates = [
    {
        "name": "Марат",
        "surname": "Дреев",
        "group": "БУЬ2358",
        "marks": [4, 5, 5]
    },
    {
        "name": "Алиса",
        "surname": "Завьялова",
        "group": "ВДО42976",
        "marks": [5, 4, 5]
    },
    {
        "name": "Данила",
        "surname": "Иванов",
        "group": "БСТ2203",
        "marks": [5, 5, 5]
    },
    {
        "name": "Михаил",
        "surname": "Ильин",
        "group": "УАТОУ4412",
        "marks": [4, 3, 4]
    },
    {
        "name": "Денис",
        "surname": "Истомин",
        "group": "ДЛУОА29401",
        "marks": [3, 3, 5]
    }
];
var rpad = function(str, length) {
	// JS не поддерживает добавление нужного количества символов
	// Справа от строки, т.е. аналога ljust из Python здесь нет 
	str = str.toString(); // Преобразование в строку
	while (str.length < length)
	str = str + ' '; // Добавление пробела в конец строки
	return str; // Когда все пробелы добавлены, возвратить строку
};
var printStudents = function(students){ 
	console.log(
		rpad("Имя", 15),
		rpad("Фамилия", 15),
		rpad("Группа", 8),
		rpad("Оценки", 20)
	);
	// Был выведен заголовок таблицы
	for (var i = 0; i<=students.length-1; i++){
		// В цикле выводится каждый экземпляр студента 
		console.log(
			rpad(students[i]['name'], 15),
			rpad(students[i]['surname'], 15),
			rpad(students[i]['group'], 8),
			rpad(students[i]['marks'], 20)
		);
	}
	console.log('\n'); // Добавляется пустая строка в конце вывода
};
// Фильтрация по группе
var filterByGroup = function(students, groupName) {
    return students.filter(function(student) {
        return student.group.toLowerCase() === groupName.toLowerCase();
    });
};
// Фильтрация по средней оценке
var filterByAverageMark = function(students, minAverage) {
    return students.filter(function(student) {
        var average = student.marks.reduce((a, b) => a + b, 0) / student.marks.length;
        return average > minAverage;
    });
};
// Получение ввода от пользователя
var getUserInput = function(promptText) {
    return prompt(promptText);
};
// Функция для демонстрации фильтра по группе
var groupFilter = function() {
    var groupFilter = getUserInput("Введите название группы для фильтрации:");
    var filteredByGroup = filterByGroup(groupmates, groupFilter);
    console.log("Студенты группы '" + groupFilter + "':");
    if (filteredByGroup.length > 0) {
        printStudents(filteredByGroup);
    } else {
        console.log("Студентов в данной группе не найдено.\n");
    }
};
// Функция для демонстрации фильтра по среднему баллу
var markFilter = function() {
    var minAverageInput = getUserInput("Введите минимальный средний балл для фильтрации:");
    var minAverage = parseFloat(minAverageInput);
    if (!isNaN(minAverage)) {
        var filteredByMark = filterByAverageMark(groupmates, minAverage);
        console.log("Студенты со средним баллом выше " + minAverage + ":");
        if (filteredByMark.length > 0) {
            printStudents(filteredByMark);
        } else {
            console.log("Студентов с таким средним баллом не найдено.\n");
        }
    } else {
        console.log("Некорректный ввод среднего балла.\n");
    }
};
