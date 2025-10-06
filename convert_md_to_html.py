#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động chuyển đổi tất cả bài giải Markdown sang HTML
Tích hợp vào file index.html
"""

import re
import os

def markdown_to_html(md_text):
    """Convert markdown to HTML"""
    
    # Headers
    md_text = re.sub(r'^### (.*?)$', r'<h4>\1</h4>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*?)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.*?)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    
    # Bold
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_text)
    
    # Lists
    lines = md_text.split('\n')
    html_lines = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('+ '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            item = line.strip()[2:]
            html_lines.append(f'<li>{item}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)
    
    if in_list:
        html_lines.append('</ul>')
    
    return '\n'.join(html_lines)

def extract_exercises(md_file):
    """Extract exercises from markdown file"""
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    exercises = []
    
    # Pattern để tìm bài tập
    pattern = r'###\s*\*\*BÀI\s+([\d.]+):\*\*\s*(.*?)(?=###\s*\*\*BÀI|$)'
    
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        exercise_num = match.group(1)
        exercise_content = match.group(2).strip()
        
        # Extract title (first line)
        lines = exercise_content.split('\n')
        title = lines[0].strip() if lines else "Bài tập"
        
        # Extract problem (từ đề bài đến GIẢI)
        problem_match = re.search(r'^(.*?)(?=\*\*GIẢI:\*\*|$)', exercise_content, re.DOTALL)
        problem = problem_match.group(1).strip() if problem_match else ""
        
        # Extract solution (sau GIẢI)
        solution_match = re.search(r'\*\*GIẢI:\*\*(.*?)(?=\*\*Đáp số:\*\*)', exercise_content, re.DOTALL)
        solution = solution_match.group(1).strip() if solution_match else ""
        
        # Extract answer
        answer_match = re.search(r'\*\*Đáp số:\*\*(.*?)$', exercise_content, re.DOTALL)
        answer = answer_match.group(1).strip() if answer_match else ""
        
        exercises.append({
            'num': exercise_num,
            'title': title,
            'problem': problem,
            'solution': solution,
            'answer': answer
        })
    
    return exercises

def generate_accordion_html(exercises):
    """Generate accordion HTML for exercises"""
    
    html_parts = []
    
    for ex in exercises:
        html = f'''
        <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAccordion(this)">
                <span>📝 Bài {ex['num']}: {ex['title']}</span>
                <span class="accordion-icon">▼</span>
            </div>
            <div class="accordion-content">
                <div class="accordion-body">
                    <div class="problem">
                        <div class="problem-title">Đề bài:</div>
                        {markdown_to_html(ex['problem'])}
                    </div>
                    
                    <div class="solution">
                        <h4>Lời giải chi tiết:</h4>
                        {markdown_to_html(ex['solution'])}
                    </div>
                    
                    <div class="answer">
                        ✅ Đáp số: {markdown_to_html(ex['answer'])}
                    </div>
                </div>
            </div>
        </div>
        '''
        html_parts.append(html)
    
    return '\n'.join(html_parts)

def main():
    """Main function"""
    
    print("🚀 Bắt đầu chuyển đổi Markdown sang HTML...")
    
    # Danh sách các file Markdown
    md_files = [
        'BAI_GIAI_XAC_XUAT_THONG_KE.md',
        'CHUONG_2_3_4_BAI_GIAI.md',
        'CHUONG_2_FINAL_CHUONG_3_4.md',
        'CHUONG_5_KIEM_DINH_GIA_THIET.md'
    ]
    
    all_exercises = {}
    
    for md_file in md_files:
        if os.path.exists(md_file):
            print(f"📄 Đang xử lý: {md_file}")
            exercises = extract_exercises(md_file)
            
            for ex in exercises:
                all_exercises[ex['num']] = ex
            
            print(f"   ✅ Tìm thấy {len(exercises)} bài tập")
    
    print(f"\n📊 Tổng số bài tập: {len(all_exercises)}")
    
    # Generate HTML
    html_content = generate_accordion_html(list(all_exercises.values()))
    
    # Save to file
    output_file = 'all_exercises.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Hoàn thành! Kết quả lưu tại: {output_file}")
    print(f"📋 Bạn có thể copy nội dung file này vào index.html")

if __name__ == '__main__':
    main()

